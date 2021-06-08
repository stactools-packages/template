# stactools-subpackage-template

Template repostitory for [stactools](https://github.com/stac-utils/stactools) subpackages.

## How to use

1. Clone this repository and name it `stactools-{NAME}`, where `NAME` is your subpackage name.
   This name should be short, memorable, and a valid Python package name (i.e. it shouldn't start with a number, etc).
2. Update `setup.cfg` with your package name, description, and such.
3. Rename `src/stactools/subpackage` to `src/stactools/{NAME}`.
4. Rewrite this README to provide information about how to use your subpackage.