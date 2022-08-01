import configparser

import pytest

from tools.perkele.tests.utils import assert_unit_file, here


def test_file_postgresql_main_service_template() -> None:
    with assert_unit_file(here('postgresql@12-main.*.service')) as config:
        with pytest.raises(configparser.NoOptionError):
            config.get('Service', 'Restart')
        with pytest.raises(configparser.NoOptionError):
            config.get('Service', 'RestartPreventExitStatus')
        config['Service']['Restart'] = 'on-failure'
        config['Service']['RestartPreventExitStatus'] = 'SIGINT SIGTERM'
        assert config.get('Service', 'Restart') == 'on-failure'
        assert config.get('Service', 'RestartPreventExitStatus') == 'SIGINT SIGTERM'
