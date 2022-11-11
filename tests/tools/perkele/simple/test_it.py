from tests.tools.perkele.utils import assert_config, assert_gets, assert_unit_file, here
from tools.perkele.unit_parser import UnitParser


def test_file_simple_service() -> None:
    gets = [
        ('Unit', 'Description', 'My Service'),
        ('Service', 'ExecStart', '/usr/bin/my-service'),
        ('Install', 'WantedBy', 'multi-user.target'),
    ]
    with assert_unit_file(here('simple.service')) as config:
        assert_gets(config, gets)


def test_writing_simple_service_with_setters() -> None:
    config = UnitParser()
    config.add_section('Unit')
    config['Unit']['Description'] = 'My Service'
    config.add_section('Service')
    config['Service']['ExecStart'] = '/usr/bin/my-service'
    config.add_section('Install')
    config['Install']['WantedBy'] = 'multi-user.target'
    assert_config(config, here('simple.service'))


def test_writing_simple_service_with_dictionary() -> None:
    config = UnitParser()
    config.read_dict(
        {
            'Unit': {'Description': 'My Service'},
            'Service': {'ExecStart': '/usr/bin/my-service'},
            'Install': {'WantedBy': 'multi-user.target'},
        },
    )
    assert_config(config, here('simple.service'))
