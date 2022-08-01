from tools.perkele.tests.utils import assert_gets, assert_unit_file, here


def test_file_httpd_service() -> None:
    gets = [
        ('Unit', 'Description', 'Some HTTP server'),
        ('Unit', 'After', 'remote-fs.target sqldb.service memcached.service'),
        ('Unit', 'Requires', 'sqldb.service memcached.service'),
        ('Unit', 'AssertPathExists', '/srv/www'),
    ]
    with assert_unit_file(here('httpd.*.service')) as config:
        assert_gets(config, gets)
