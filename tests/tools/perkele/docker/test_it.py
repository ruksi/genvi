from tests.tools.perkele.utils import assert_gets, assert_unit_file, here


def test_file_docker_service() -> None:
    with assert_unit_file(here('docker.*.service')) as config:
        assert_gets(config, [])
