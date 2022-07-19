from typing import List, Optional

import pytest
from _pytest.monkeypatch import MonkeyPatch

from myproject.console.settings import parse_settings


@pytest.mark.parametrize(
    ('arguments', 'log_level'),
    [
        ([], 'INFO'),
        (['-v'], 'DEBUG'),
        (['-q'], 'WARNING'),
        (['-qq'], 'ERROR'),
    ],
)
def test_log_level(arguments: List[str], log_level: Optional[str]) -> None:
    assert parse_settings(arguments).log_level == log_level


@pytest.mark.parametrize('log_level', ['warning', 'Warning', 'WARNING'])
def test_log_level_overrides_env_var(monkeypatch: MonkeyPatch, log_level: str) -> None:
    assert parse_settings([]).log_level == 'INFO'
    assert parse_settings(['-v']).log_level == 'DEBUG'
    assert parse_settings(['-qq']).log_level == 'ERROR'
    monkeypatch.setenv('LOGLEVEL', log_level)
    assert parse_settings([]).log_level == 'WARNING'
    assert parse_settings(['-v']).log_level == 'DEBUG'
    assert parse_settings(['-qq']).log_level == 'ERROR'
