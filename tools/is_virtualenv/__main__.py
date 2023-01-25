import sys

from tools.is_virtualenv.core import is_virtualenv

if __name__ == "__main__":
    sys.stdout.write(f"{is_virtualenv()}\n")  # type: ignore[no-untyped-call]
