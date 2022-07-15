import shutil
from pathlib import Path

from magic.utils.config import Config
from magic.utils.errors import ValidationError
from magic.utils.files import (
    generate_readme,
    rename_package,
    strip_lines_between_markers,
)

ErrorCode = int


def main(config: Config) -> ErrorCode:
    try:
        config.validate()
    except ValidationError as exception:
        print('error:', exception)  # noqa: T201
        return 1

    rename_package(config)
    strip_lines_between_markers(
        target=Path(config.genvi_root, 'Makefile'),
        start='# -->',
        end='# <--',
    )
    strip_lines_between_markers(
        target=Path(config.genvi_root, '.github/workflows/ci.yml'),
        start='# -->',
        end='# <--',
    )

    readme = Path(config.genvi_root, 'README.md')
    readme.unlink()
    with readme.open(encoding='utf-8', mode='w') as file:
        file.write(generate_readme(config))

    # bibbidi-bobbidi-poof!
    shutil.rmtree(Path(config.genvi_root, 'magic'))
    shutil.rmtree(Path(config.genvi_root, 'images'))
    Path(config.genvi_root, 'ABOUT.md').unlink()
    return 0
