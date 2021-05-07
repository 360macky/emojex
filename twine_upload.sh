#!/usr/bin/env bash

# Build the distribution.
python3 setup.py sdist bdist_wheel

# Upload with twine.
twine upload dist/* --username $PYPI_USERNAME --password $PYPI_PASSWORD
