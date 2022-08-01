from tools.perkele.tests.utils import assert_gets, assert_unit_file, here


def test_file_reap_service() -> None:
    gets = [
        ('Unit', 'Description', 'Remove Stale Online ext4 Metadata Check Snapshots'),
        ('Unit', 'ConditionCapability', ('CAP_SYS_ADMIN', 'CAP_SYS_RAWIO')),
        ('Unit', 'Documentation', 'man:e2scrub_all(8)'),
        ('Service', 'Type', 'oneshot'),
        ('Install', 'WantedBy', 'default.target'),
    ]
    with assert_unit_file(here('reap.service')) as config:
        assert_gets(config, gets)
