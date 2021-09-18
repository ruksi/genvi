import io

from _pytest.capture import CaptureFixture

from myproject.console.executable import main


def test_executable_default(capsys: CaptureFixture[str]) -> None:
    assert main() == 0
    captured = capsys.readouterr()
    assert 'mock command line interface:' in captured.out


def test_executable_custom_file() -> None:
    string_io = io.StringIO()
    assert main(text_io=string_io) == 0
    string_io.seek(0)
    output = string_io.read()
    assert 'mock command line interface:' in output
