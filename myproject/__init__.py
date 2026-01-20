from pathlib import Path

version_path = Path(Path(__file__).parent, "VERSION")  # noqa: RUF067
__version__ = version_path.read_text(encoding="utf-8").strip()
