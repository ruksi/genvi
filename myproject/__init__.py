from pathlib import Path

with Path(Path(__file__).parent, 'VERSION').open(encoding='utf-8') as version_file:
    __version__ = version_file.read().strip()
