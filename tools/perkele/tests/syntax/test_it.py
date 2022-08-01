from tools.perkele.tests.utils import assert_config, assert_gets, assert_unit_file, here
from tools.perkele.unit_parser import UnitParser


def test_backslashes() -> None:
    gets = [
        ('Section A', 'KeyOne', 'value 1'),
        ('Section A', 'KeyTwo', 'value 2'),
        ('Section B', 'Setting', '"something" "some thing" "…"'),
        ('Section B', 'KeyTwo', 'value 2 \\ value 2 continued'),
        ('Section C', 'KeyThree', 'value 3\\ value 3 continued'),
    ]
    with assert_unit_file(here('backslashes.*.ini')) as config:
        assert_gets(config, gets)


def test_duplicate_directives() -> None:
    gets = [
        ('Service', 'Type', 'oneshot'),
        (
            'Service',
            'ExecStart',
            ('/bin/echo ${ONE} ${TWO} ${THREE}', '/bin/echo $ONE $TWO $THREE'),
        ),
        ('Service', 'Environment', 'ONE=\'one\' "TWO=\'two two\' too" THREE='),
    ]
    with assert_unit_file(here('duplicate-directive.*.service')) as config:
        assert_gets(config, gets)


def test_list_reset() -> None:
    gets = [
        ('Service', 'Type', 'oneshot'),
        (
            'Service',
            'ExecStart',
            ('', '/bin/echo hello', '/bin/echo bye', '', '/bin/echo HIYA'),
        ),
    ]
    with assert_unit_file(here('list-reset.*.service')) as config:
        assert_gets(config, gets)


def test_writing_no_value() -> None:
    # no value definitions (`ExecStart`, not `ExecStart=`) are
    # rarely, if ever, used with unit files though
    config = UnitParser(allow_no_value=True)
    config.read_dict(
        {
            'Section A': {
                'OptionOne': 'value 1',
                'OptionTwo': None,  # no value definition
                'OptionThree': '',  # empty (string) value definition
            },
        },
    )
    assert_config(config, here('no-value.ini'))


def test_semicolons() -> None:
    gets = [
        ('Service', 'Type', 'oneshot'),
        ('Service', 'ExecStart', 'echo one ; echo "two two"'),
    ]
    with assert_unit_file(here('semicolons.*.service')) as config:
        assert_gets(config, gets)
