from tests.tools.perkele.utils import assert_gets, assert_unit_file, here


def test_file_ubuntu_report_path() -> None:
    with assert_unit_file(here('ubuntu-report.path')) as config:
        assert_gets(config, [])
