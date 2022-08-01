from tools.perkele.tests.utils import assert_gets, assert_unit_file, here


def test_file_default_target() -> None:
    gets = [
        ('Unit', 'Description', 'Graphical Interface'),
        ('Unit', 'Documentation', 'man:systemd.special(7)'),
        ('Unit', 'Requires', 'multi-user.target'),
        ('Unit', 'Wants', 'display-manager.service'),
        ('Unit', 'Conflicts', 'rescue.service rescue.target'),
        (
            'Unit',
            'After',
            'multi-user.target rescue.service rescue.target display-manager.service',
        ),
        ('Unit', 'AllowIsolate', 'yes'),
    ]
    with assert_unit_file(here('default.target')) as config:
        assert_gets(config, gets)
