import inspect
import io
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, Iterable, Sequence, Tuple, Union

from typing_extensions import TypeAlias

from tools.perkele.unit_parser import UnitParser

GetSpec: TypeAlias = Iterable[Tuple[str, str, Union[str, Sequence[str]]]]


def assert_gets(config: UnitParser, get_spec: GetSpec) -> None:
    for get in get_spec:
        assert config.get(get[0], get[1]) == get[2]


@contextmanager
def assert_unit_file(location: str) -> Generator[UnitParser, None, None]:
    """
    Open, yield and finally verify a `systemd` unit file in the given location.

    If `location` contains an asterisk `*`, it will be replaced `in` for input
    (the original unit file) and `out` for output (expected write after the tests).
    For example `server.*.service` becomes `server.in.service` and `server.out.service`.

    Otherwise, the input file is expected to also be the output, meaning that the
    file will remain unchanged if read, deserialized, tested, serialized and written.
    """
    if '*' in location:
        in_location = location.replace('*', 'in')
        out_location = location.replace('*', 'out')
    else:
        in_location = location
        out_location = location
    config = UnitParser()
    config.read(in_location)
    yield config
    assert_config(config, out_location)


def assert_config(config: UnitParser, location: str) -> None:
    results = io.StringIO()
    config.write(results)
    results.seek(0)
    with open(location, encoding='utf-8') as out_file:
        assert results.read() == out_file.read()


def here(location: str) -> str:
    stack = inspect.stack()
    caller = next(context for context in stack if context.filename != __file__)
    return str(Path(Path(caller.filename).parent, location).absolute())
