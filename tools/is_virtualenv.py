import sys

# Tools for checking if Python process is in a virtual environment.
# This is intentionally missing type hints for it to work on Python 2.
# Source: https://stackoverflow.com/a/1883251


def get_base_prefix_compat():  # type: ignore[no-untyped-def]
    return (
        getattr(sys, 'base_prefix', None)
        or getattr(sys, 'real_prefix', None)
        or sys.prefix
    )


def is_virtualenv():  # type: ignore[no-untyped-def]
    return get_base_prefix_compat() != sys.prefix  # type: ignore[no-untyped-call]


if __name__ == '__main__':
    sys.stdout.write(f'{is_virtualenv()}\n')  # type: ignore[no-untyped-call]
