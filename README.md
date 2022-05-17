# stactools-template

This is a template repo used for creating new packages for `stactools`.

## How to use

1. Clone this template repository as your package name, e.g. `landsat`.
   This name should be short, memorable, and a valid Python package name (i.e. it shouldn't start with a number, etc). It can, however, include a hyphen, in which case the name for Python imports will be the underscored version, e.g. `landsat-8` goes to `stactools.landsat_8`.
   Your name will be used on PyPI to publish the package in the stactools namespace, e.g. `stactools-landsat`.
2. Change into the top-level directory of your package and run `scripts/rename`.
   This will update _most_ of the files in the repository with your new package name.
3. Update `setup.cfg` with your package description and such.
4. Update the LICENSE with your company's information (or whomever holds the copyright).
5. Install the package (`pip install -e .`), development requirements (`pip install -r requirements-dev.txt`), and pre-commit (`pre-commit install`).
6. Edit or replace the existing functions to create stac Items and Collections for your dataset.
6. Add example Items (and Collections and Catalogs, if included) to an `examples/` directory.
7. Delete this file, and rename `README-template.md` to `README.md`. Update your new README to provide information about how to use your package.
