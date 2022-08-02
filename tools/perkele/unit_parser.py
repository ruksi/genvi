import configparser
import itertools
from collections import OrderedDict
from typing import Any, Callable, Iterable, List, Optional, Tuple, TypeVar, Union

from typing_extensions import Protocol, TypeAlias

DirectiveKey: TypeAlias = str
DirectiveValue: TypeAlias = Union[None, str, Tuple[Optional[str], ...]]
SectionItems: TypeAlias = Iterable[Tuple[DirectiveKey, DirectiveValue]]

T = TypeVar('T')
T_contra = TypeVar('T_contra', contravariant=True)


class SupportsWrite(Protocol[T_contra]):
    def write(self, s: T_contra) -> Any:  # type: ignore[misc] # noqa: PLC0103, PLW0613
        """Write the given thing to somewhere."""


DUPLICATE_MARKER = object()


class UnitParserDict(OrderedDict):  # type: ignore[type-arg]
    """A custom dictionary to reimplement the standard library config parser logic."""

    def __setitem__(self, key: str, value: Any) -> None:  # type: ignore[misc]
        if isinstance(value, list) and key in self and isinstance(self[key], list):
            # all ini file option values are fed as lists on the initial read,
            # use tuples as a special type that signifies duplicate key definitions
            # and hope that no other part of config parser uses lists for anything
            if self[key][0] != DUPLICATE_MARKER:
                super().__setitem__(key, [DUPLICATE_MARKER] + self[key] + value)
            else:
                super().__setitem__(key, self[key] + value)
            return
        super().__setitem__(key, value)


def pop_until(items: List[T], condition: Callable[[T], bool]) -> None:
    while not condition(items[-1]):
        items.pop()


class UnitParser(configparser.ConfigParser):
    """
    Config parser for `systemd` unit files.

    Unit files are Windows `.ini` and XDG `.desktop` inspired configs for `systemd`.

    The main difference is that some directives can be specified more than once,
    in which case the value will be converted to a tuple of strings so the original
    formatting can be reconstructed after parsing.

    Caveats:
    * Read-to-Write will remove all comments.
    * Read-to-Write will normalize indentation to 1 space if any was used.
    * Read-to-Write will group keys duplicates even if originally separate.
    """

    _writing_first_section = True

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # type: ignore[misc]
        # unit files can contain duplicate option names in the same section
        kwargs.setdefault('strict', False)
        # empty lines are ignored in unit files, but there can be comments lines
        # inside backslash concatenation, which are treated similarly to empty lines
        kwargs.setdefault('empty_lines_in_values', True)
        # unit file key-value pairs are always delimited with `=`
        kwargs.setdefault('delimiters', ('=',))
        # don't do any interpolation by default, it messes with values containing %
        kwargs.setdefault('interpolation', configparser.Interpolation())
        # use a custom ordered dict to reimplement parts of the config parser logic
        kwargs.setdefault('dict_type', UnitParserDict)
        super().__init__(*args, **kwargs)
        # don't lowercase option keys
        self.optionxform = lambda option: option  # type: ignore[assignment]

    def _join_multiline_values(self) -> None:
        defaults = (
            self.default_section,
            self._defaults,  # type: ignore[attr-defined]
        )
        all_sections = itertools.chain(
            (defaults,),
            self._sections.items(),  # type: ignore[attr-defined]
        )
        for section, options in all_sections:
            for name, val in options.items():
                if val[0] == DUPLICATE_MARKER:
                    val.pop(0)
                    pop_until(val, lambda item: bool(item != ''))
                    val = tuple(v.rstrip() for v in val)
                else:
                    val = ' '.join(val).rstrip()
                options[name] = self._interpolation.before_read(  # type: ignore[attr-defined] # noqa: E501
                    self,
                    section,
                    name,
                    val,
                )

    def write(
        self,
        fp: SupportsWrite[str],
        space_around_delimiters: bool = False,
    ) -> None:
        self._writing_first_section = True
        super().write(fp, space_around_delimiters=space_around_delimiters)

    def _write_section(
        self,
        fp: SupportsWrite[str],
        section_name: str,
        section_items: SectionItems,
        delimiter: str,
    ) -> None:
        # don't start with an unnecessary empty line
        if self._writing_first_section:
            self._writing_first_section = False
        else:
            fp.write('\n')

        fp.write(f'[{section_name}]\n')
        for key, values in section_items:
            # handling for our tuple hack for duplicate key support
            if isinstance(values, str) or values is None:
                values = (values,)
            for value in values:
                value = self._interpolation.before_write(  # type: ignore[attr-defined]
                    self,
                    section_name,
                    key,
                    value,
                )
                if value is None and self._allow_no_value:  # type: ignore[attr-defined]
                    value = ''
                else:
                    value = delimiter + str(value).replace('\n', '\n\t')

                # format line wrapping backslashes properly
                value = value.replace('\\', '\\\n')
                fp.write(f'{key}{value}\n')
