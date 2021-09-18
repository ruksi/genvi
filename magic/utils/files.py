import shutil
from pathlib import Path
from string import Template

from magic.utils.config import Config
from magic.utils.consts import DEFAULT_AUTHOR, DEFAULT_EMAIL, DEFAULT_PACKAGE_NAME


def rename_package(config: Config) -> None:
    package_dir = Path(config.genvi_root, DEFAULT_PACKAGE_NAME)
    test_dir = Path(config.genvi_root, 'tests')
    files_to_search_and_replace = (
        list(package_dir.glob('**/*.py'))
        + list(test_dir.glob('**/*.py'))
        + [
            Path(config.genvi_root, '.github/workflows/ci.yml'),
            Path(config.genvi_root, 'LICENSE'),
            Path(config.genvi_root, 'MANIFEST.in'),
            Path(config.genvi_root, 'Makefile'),
            Path(config.genvi_root, 'pyproject.toml'),
            Path(config.genvi_root, 'setup.cfg'),
        ]
    )

    for filename in files_to_search_and_replace:
        with Path(filename).open(encoding='utf-8') as file:
            contents = file.read()
        with Path(filename).open(encoding='utf-8', mode='wt') as file:
            contents = contents.replace(DEFAULT_PACKAGE_NAME, config.name)
            if config.author:
                contents = contents.replace(DEFAULT_AUTHOR, config.author)
            if config.email:
                contents = contents.replace(DEFAULT_EMAIL, config.email)
            file.write(contents)

    shutil.move(
        str(package_dir),
        Path(config.genvi_root, config.name),
    )


def generate_readme(config: Config) -> str:
    substitutes = {
        'name': config.name,
    }
    with Path(Path(__file__).parent, 'readme_template.md').open(
        encoding='utf-8',
    ) as file:
        tmpl = Template(file.read())
        return tmpl.substitute(substitutes)


def strip_lines_between_markers(target: Path, start: str, end: str) -> None:
    lines = []
    with target.open(encoding='utf-8') as file:
        keeping = True
        for line in file.readlines():
            if line.startswith(start):
                keeping = False
            if line.startswith(end):
                keeping = True
                continue
            if keeping:
                lines.append(line)
    with target.open(encoding='utf-8', mode='w') as file:
        file.writelines(lines)
