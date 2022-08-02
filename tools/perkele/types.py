from typing import Any, Iterable, Optional, Tuple, TypeVar, Union

from typing_extensions import Protocol, TypeAlias

DirectiveKey: TypeAlias = str
DirectiveValue: TypeAlias = Union[None, str, Tuple[Optional[str], ...]]
SectionItems: TypeAlias = Iterable[Tuple[DirectiveKey, DirectiveValue]]

T_contra = TypeVar('T_contra', contravariant=True)


class SupportsWrite(Protocol[T_contra]):
    def write(self, s: T_contra) -> Any:  # type: ignore[misc] # noqa: PLC0103, PLW0613
        """Write the given thing to somewhere."""
