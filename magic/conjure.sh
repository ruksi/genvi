#!/usr/bin/env bash
set -euo pipefail

# A quickstart script for https://github.com/ruksi/genvi

# these version checks will stop the script if missing the dependency
git --version
make --version
python --version

echo "Creating a new directory for a Python project."
read -r -p "Package name: " PACKAGE < /dev/tty
git clone git@github.com:ruksi/genvi.git "$PACKAGE"
cd "$PACKAGE"
rm -rf .git/
make package="$PACKAGE"
