#!/usr/bin/env bash
set -euo pipefail

# A quickstart script for https://github.com/ruksi/genvi

# these version checks will stop the script if missing the dependency
git --version
python --version

echo "Creating a new directory for a Python project."
read -r -p "Project name (also the lowercase name of the directory): " PROJECT < /dev/tty
git clone git@github.com:ruksi/genvi.git "$PROJECT"
cd "$PROJECT"
python -m magic
