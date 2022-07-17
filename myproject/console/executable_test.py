from _pytest.capture import CaptureFixture
from pytest_mock import MockFixture

from myproject.console.executable import main


def test_main_success(capsys: CaptureFixture[str]) -> None:
    assert main() == 0
    standard = capsys.readouterr()
    assert 'mock command line interface:' in standard.out
    assert '' == standard.err


def test_main_failure(capsys: CaptureFixture[str], mocker: MockFixture) -> None:
    msg = 'boom things went wrong'
    mocker.patch('myproject.console.executable.run').side_effect = Exception(msg)
    assert main() == 1
    standard = capsys.readouterr()
    assert '' == standard.out
    assert f'{msg}\n' == standard.err
