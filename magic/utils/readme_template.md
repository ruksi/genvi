
# `$name`

## Development

Setup development environment:

```bash
make venv
source venv/bin/activate
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

The following PyCharm integrations make development flow smoother by giving errors
interactively while developing and makes it easy to jump to specific error locations.

Bring `flake8` lint highlights to PyCharm:

* Figure out where the `flake8-for-pycharm` executable is e.g.

  ```bash
  which flake8_pycharm.py
  # e.g. /projects/$name/venv/bin/flake8_pycharm.py
  ```

* Install **Pylint** plugin to PyCharm using the marketplace
* Configure `Settings > Pylint`:
  * Path to Pylint executable: *`flake8_pycharm.py` full path*
  * Path to pylintrc: */projects/$name/setup.cfg* (i.e. `flake8` config)

Bring `mypy` type checks to PyCharm:

* Install **Mypy** plugin to PyCharm using the marketplace
  * Not the *Mypy (Official)*, that is outdated and inferior
* Configure `Settings > Mypy`:
  * Path to Mypy executable: */projects/$name/venv/bin/mypy* (should detect)
  * Arguments: *--install-types --scripts-are-modules*

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

## Production

Setup production environment:

```bash
NO_VENV=1 make prod

# or, if a virtual environment is wanted
make venv
source venv/bin/activate
make prod
```
