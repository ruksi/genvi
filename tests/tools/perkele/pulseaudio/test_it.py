from tests.tools.perkele.utils import assert_gets, assert_unit_file, here


def test_file_pulseaudio_service() -> None:
    gets = [
        ('Unit', 'Description', 'Sound Service'),
        ('Unit', 'Requires', 'pulseaudio.socket'),
        ('Unit', 'ConditionUser', '!root'),
        (
            'Service',
            'ExecStart',
            '/usr/bin/pulseaudio --daemonize=no --log-target=journal',
        ),
        ('Service', 'LockPersonality', 'yes'),
        ('Service', 'MemoryDenyWriteExecute', 'yes'),
        ('Service', 'NoNewPrivileges', 'yes'),
        ('Service', 'Restart', 'on-failure'),
        ('Service', 'RestrictNamespaces', 'yes'),
        ('Service', 'SystemCallArchitectures', 'native'),
        ('Service', 'SystemCallFilter', '@system-service'),
        ('Service', 'Type', 'notify'),
        ('Service', 'UMask', '0077'),
        ('Install', 'Also', 'pulseaudio.socket'),
        ('Install', 'WantedBy', 'default.target'),
    ]
    with assert_unit_file(here('pulseaudio.*.service')) as config:
        assert_gets(config, gets)


def test_file_pulseaudio_socket() -> None:
    gets = [
        ('Unit', 'Description', 'Sound System'),
        ('Unit', 'ConditionUser', '!root'),
        ('Socket', 'Priority', '6'),
        ('Socket', 'Backlog', '5'),
        ('Socket', 'ListenStream', '%t/pulse/native'),
        ('Install', 'WantedBy', 'sockets.target'),
    ]
    with assert_unit_file(here('pulseaudio.socket')) as config:
        assert_gets(config, gets)
