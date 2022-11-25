#!/usr/bin/env bash
set -euo pipefail

# A quickstart script for https://github.com/ruksi/genvi

# these version checks will stop the script if missing the dependency
git --version
make --version
python --version

echo "Creating a new directory for a Python project."
read -r -p "Package Name (lowercase letters, no special characters of any kind): " PACKAGE < /dev/tty
read -r -p "Author Name: " AUTHOR < /dev/tty
read -r -p "Author Email: " EMAIL < /dev/tty
git clone git@github.com:ruksi/genvi.git "$PACKAGE"
cd "$PACKAGE"
make package="$PACKAGE" author="$AUTHOR" email="$EMAIL"
