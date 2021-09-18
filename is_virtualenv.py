import sys

# Tools for checking if Python process is in a virtual environment.
# Source: https://stackoverflow.com/a/1883251


def get_base_prefix_compat() -> str:
    return (
        getattr(sys, 'base_prefix', None)
        or getattr(sys, 'real_prefix', None)
        or sys.prefix
    )


def is_virtualenv() -> bool:
    return get_base_prefix_compat() != sys.prefix


if __name__ == '__main__':
    print(is_virtualenv())
