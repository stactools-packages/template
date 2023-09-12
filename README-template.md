# stactools-ephemeral

[![PyPI](https://img.shields.io/pypi/v/stactools-ephemeral?style=for-the-badge)](https://pypi.org/project/stactools-ephemeral/)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/stactools-packages/ephemeral/continuous-integration.yml?style=for-the-badge)

- Name: ephemeral
- Package: `stactools.ephemeral`
- [stactools-ephemeral on PyPI](https://pypi.org/project/stactools-ephemeral/)
- Owner: @githubusername
- [Dataset homepage](http://example.com)
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields:
  - `ephemeral:custom`: A custom attribute
- [Browse the example in human-readable form](https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/stactools-packages/ephemeral/main/examples/collection.json)

A short description of the package and its usage.

## STAC examples

- [Collection](examples/collection.json)
- [Item](examples/item/item.json)

## Installation

```shell
pip install stactools-ephemeral
```

## Command-line usage

Description of the command line functions

```shell
stac ephemeral create-item source destination
```

Use `stac ephemeral --help` to see all subcommands and options.

## Contributing

We use [pre-commit](https://pre-commit.com/) to check any changes.
To set up your development environment:

```shell
pip install -e '.[dev]'
pre-commit install
```

To check all files:

```shell
pre-commit run --all-files
```

To run the tests:

```shell
pytest -vv
```

If you've updated the STAC metadata output, update the examples:

```shell
scripts/update-examples
```
