# stactools-package

- Name: package
- Package: `stactools.package`
- PyPI: https://pypi.org/project/stactools-package/
- Owner: @githubusername
- Dataset homepage: http://example.com
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields:
  - `package:custom`: A custom attribute

A short description of the package and its usage.

## How to use

1. Clone this template repository as your package name, e.g. `landsat`.
   This name should be short, memorable, and a valid Python package name (i.e. it shouldn't start with a number, etc).
   It can, however, include a hyphen, in which case the name for Python imports will be the underscored version, e.g. `landsat-8` goes to `stactools.landsat_8`.
   Your name will be used on PyPI to publish the package in the stactools namespace, e.g. `stactools-landsat`.
2. Change into the top-level directory of your package and run `scripts/rename`.
   This will update _most_ of the files in the repository with your new package name.
   You'll have to manually update `setup.cfg` and `README.md`. 
3. Update `setup.cfg` with your package name, description, and such.
4. Rewrite this README to provide information about how to use your package.
5. Update the LICENSE with your company's information (or whomever holds the copyright).
6. Run `sphinx-quickstart` in the `docs` directory to create the documentation template.
7. Update `docs/installation_and_basic_usage.ipynb` to provide an interactive notebook to help users get started. Include the following badge at the top of the README to launch the notebook: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/stactools-packages/template/main?filepath=docs/installation_and_basic_usage.ipynb). Be sure to modify the badge href to match your package repo.
8. Add example Items (and Collections and Catalogs, if included) to a `examples/` directory.
9. Delete this section from the README

## Examples

### STAC objects

- [Collection](examples/collection.json)
- [Item](examples/item/item.json)

### Command-line usage

Description of the command line functions

```bash
$ stac package create-item source destination
```

Use `stac package --help` to see all subcommands and options.
