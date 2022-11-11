from tools.perkele.tests.utils import assert_gets, assert_unit_file, here


def test_redis_service() -> None:
    gets = [
        (
            'Service',
            'ReadWritePaths',
            ('-/var/lib/redis', '-/var/log/redis', '-/var/run/redis'),
        ),
    ]
    with assert_unit_file(here('redis-server.*.service')) as config:
        assert_gets(config, gets)
