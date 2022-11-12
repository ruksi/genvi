import shutil
from pathlib import Path
from string import Template

from magic.console.config import Config
from magic.utils.consts import DEFAULT_AUTHOR, DEFAULT_EMAIL, DEFAULT_PACKAGE_NAME


def rename_package(config: Config) -> None:
    package_dir = config.genvi_root / DEFAULT_PACKAGE_NAME
    test_dir = config.genvi_root / 'tests'
    files_to_search_and_replace = (
        list(package_dir.glob('**/*.py'))
        + list(test_dir.glob('**/*.py'))
        + [
            (config.genvi_root / '.github/workflows/ci.yml'),
            (config.genvi_root / 'LICENSE'),
            (config.genvi_root / 'MANIFEST.in'),
            (config.genvi_root / 'Makefile'),
            (config.genvi_root / 'pyproject.toml'),
            (config.genvi_root / 'setup.cfg'),
        ]
    )

    for file_path in files_to_search_and_replace:
        contents = file_path.read_text(encoding='utf-8')
        contents = contents.replace(DEFAULT_PACKAGE_NAME, config.name)
        if config.author:
            contents = contents.replace(DEFAULT_AUTHOR, config.author)
        if config.email:
            contents = contents.replace(DEFAULT_EMAIL, config.email)
        file_path.write_text(contents, encoding='utf-8')

    shutil.move(
        str(package_dir),
        Path(config.genvi_root, config.name),
    )


def generate_readme(config: Config) -> str:
    substitutes = {
        'name': config.name,
    }
    tmpl_path = Path(Path(__file__).parent, 'readme_template.md')
    tmpl_str = tmpl_path.read_text(encoding='utf-8')
    tmpl = Template(tmpl_str)
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
    target.write_text(''.join(lines), encoding='utf-8')
