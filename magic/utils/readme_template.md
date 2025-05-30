# `$$name`

## Development

Development requires `python>=3.9` and `make`.

Setup development environment:

```bash
# activate a virtual environment as you prefer; or simply:
make venv
source .venv/bin/activate
# install development dependencies:
make dev
```

Check code style, complexity and vulnerabilities:

```bash
make lint
```

Run tests:

```bash
make test
```

Add new dependencies:

```bash
# edit `requirements.in`
# and/or edit `requirements-dev.in`
make update
make dev lint test
```

Upgrade existing dependencies to the latest version:

```bash
make upgrade
make dev lint test
```

Resolve build issues about outdated dependency conflicts:

```bash
# edit `requirements.in` version specifications
make update dev.python dev.python.outdated
# repeat until you get no conflicts
```

### PyCharm Integrations

The following PyCharm integrations make development smoother by giving errors
interactively while developing and makes it easy to jump to specific error locations.

Bring `ruff` errors to PyCharm:

* Create a new `Settings > Tools > File Watchers`
  * Name: *ruff*
  * File type: *Python*
  * Scope: *Project Files*
  * Program: *$PyInterpreterDirectory$/ruff*
  * Arguments: *--force-exclude $FilePath$*
  * Output paths to refresh: *$FilePath$*
  * Working directory: *$ContentRoot$*
* Enable the watcher in `Settings > Tools > File Watchers`

Bring `mypy` type checks to PyCharm:

* Install **Mypy** plugin to PyCharm using the marketplace
  * Not the *Mypy (Official)*, that is outdated
* Configure `Settings > Other Settings > Mypy`:
  * Path to Mypy executable: *(should auto-detect)*
  * Arguments: *--install-types --non-interactive --scripts-are-modules*

## Testing Guidelines

All tests and testing related utilities go under the `tests` directories.
This keeps testing related code separate from the application code.

* Prefer `tests/*`,
  but `path/to/subdir/tests/*` are also acceptable if `subdir` is a well-defined whole
* This is the most common standard in the Python world and many tools assume
  this approach e.g. `pytest` fixture discovery through `conftest.py` files,
  which would lead you to add these `conftest.py` files to bizarre locations
  in your application code.
* None of the above are included in distribution builds or test coverage.

## Distribution

Release a new version:

```bash
# major (breaking changes)
# minor (new features but compatible)
# patch (other improvements and fixes)
make version bump=minor
make build
git push --follow-tags
make publish
```

To publish release notes, go to GitHub Releases and find the latest draft that
[Release Drafter](https://github.com/release-drafter/release-drafter) GitHub Action
should've been keeping updated according to the labels in pull requests merged to the master.

Check that the release draft looks correct,
change the version number to match the release and publish.
