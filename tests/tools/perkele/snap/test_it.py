from tests.tools.perkele.utils import assert_gets, assert_unit_file, here


def test_file_snap_slack_mount() -> None:
    with assert_unit_file(here('snap-slack-64.mount')) as config:
        assert_gets(config, [])
