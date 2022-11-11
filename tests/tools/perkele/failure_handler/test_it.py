from tests.tools.perkele.utils import assert_gets, assert_unit_file, here


def test_file_failure_handler_service_template() -> None:
    gets = [
        ('Unit', 'Description', 'My failure handler for %i'),
        ('Service', 'Type', 'oneshot'),
        ('Service', 'ExecStart', '/usr/sbin/handler %i'),
    ]
    with assert_unit_file(here('failure-handler@.*.service')) as config:
        assert_gets(config, gets)
