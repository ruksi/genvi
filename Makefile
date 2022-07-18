MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:

package?=
author?=
email?=
NO_VENV?=

ifndef VERBOSE
# Usage:
#    make help            # don't print commands ran
#    VERBOSE=1 make help  # print commands ran
.SILENT:
endif


# --> THE WIZARD WILL BANISH THIS
.PHONY: wizard
wizard:
	python -m magic --name='$(package)' --author='$(author)' --email='$(email)'
	echo 'The Python project has been created'
	echo 'You may now `cd` to the project root and run `git add -A` followed by `git commit -m "Initial commit"`'
	echo 'Continue development by reading the new README.md'
# <-- THE WIZARD WILL BANISH THIS


.PHONY: help
help:
	echo 'Check README for usage examples'

.PHONY: venv
# create a virtual environment, defaults to builtin `venv` but you can use `virtualenv` package just as well
venv:
	python -m venv venv/
	echo -e '\nVirtual environment created at `venv/`; activate it with `source venv/bin/activate`'

.PHONY: ensure-venv
# abort if running outside of a virtual environment
# override with `NO_VENV=1 make ...`
ensure-venv:
	if [ $(NO_VENV) ]; then exit 0; fi;
	IS_VENV=`python tools/is_virtualenv.py`
	if [ $$IS_VENV != 'True' ]; then
		echo 'Not in a virtual environment, aborting';
		echo 'Use `NO_VENV=1 make <...>` or run `make venv` followed by activate';
		exit 1;
	fi




.PHONY: prod
# setup production environment
prod: ensure-venv
	pip install -r requirements.txt




.PHONY: dev
# setup development environment
dev: ensure-venv dev-python dev-hooks

.PHONY: dev-python
# install Python dependencies for development
dev-python: ensure-venv
	pip install -r requirements-dev.txt

.PHONY: dev-python-outdated
# install valid but outdated production requirements for development
dev-python-outdated: ensure-venv
	pip install -r requirements.out

.PHONY: dev-hooks
# install pre-commit hooks for development
dev-hooks: ensure-venv
	pre-commit install --install-hooks

.PHONY: lint
# run all project style, design and type checkers
lint: ensure-venv
	pre-commit run --all-files

.PHONY: test
# run all project unit tests and print coverage misses
test: ensure-venv
	python -m pytest --cov --cov-report=term-missing

.PHONY: coverage-data
# run all project unit tests and save coverage report for upload
coverage-data: ensure-venv
	python -m coverage run --parallel -m pytest

.PHONY: update
# update dependency definitions after .in-file modifications
update: ensure-venv
	pip-compile --no-header --allow-unsafe requirements.in
	pip-compile --no-header --allow-unsafe requirements-dev.in
	python tools/freezenuts.py requirements.in > requirements.out

.PHONY: upgrade
# upgrade all dependencies to the latest valid version
upgrade: ensure-venv
	pip-compile --upgrade --no-header --allow-unsafe requirements.in
	pip-compile --upgrade --no-header --allow-unsafe requirements-dev.in
	python tools/freezenuts.py requirements.in > requirements.out
	pre-commit autoupdate




.PHONY: run
# run package as a module
run: ensure-venv
	python -m myproject

.PHONY: install
# install the package to current the virtual environment as an editable,
# and add all the configured executables to the environment `/bin`
install: ensure-venv
	pip install -e .
	echo -e '\nTry running `myproject` in the command line'

.PHONY: uninstall
# uninstall any `pip` installation of this package, but doesn't touch dependencies
uninstall: ensure-venv
	pip uninstall -y myproject



.PHONY: version
# increment package version and create a tagged git commit
# Usage: make version bump=minor # 'major', 'minor' or 'patch'
version: ensure-venv
	python tools/bump.py myproject/__init__.py $(bump)
	git reset
	git add myproject/__init__.py
	VERSION=`python -c 'import myproject; print(myproject.__version__)'`
	git commit -m "Become $$VERSION"
	git tag -a $$VERSION -m "$$VERSION"
	echo -e '\nCreated a new tagged commit, remember to later push it with `git push --follow-tags`'

.PHONY: build
# compile the current package version as distributables under `/dist`
build: ensure-venv
	python -m build

.PHONY: publish
# upload the current version distributables to PyPI for sharing
publish: ensure-venv
	VERSION=`python -c 'import myproject; print(myproject.__version__)'`
	twine upload dist/myproject-$$VERSION*
