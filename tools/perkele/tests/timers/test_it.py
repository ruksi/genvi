from tools.perkele.tests.utils import assert_gets, assert_unit_file, here


def test_file_monotonic_timer() -> None:
    gets = [('Timer', 'OnBootSec', '15min')]
    with assert_unit_file(here('monotonic.*.timer')) as config:
        assert_gets(config, gets)


def test_file_realtime_timer() -> None:
    gets = [('Timer', 'OnCalendar', 'weekly')]
    with assert_unit_file(here('realtime.*.timer')) as config:
        assert_gets(config, gets)
