#!/bin/sh

# Stop on problems.
set -e

cd `dirname $0`

# Target git master using BIOBLEND_TARGET=git+git://github.com/galaxyproject/bioblend.git@master start_tutorial.sh
BIOBLEND_TARGET="${BIOBLEND_TARGET:-bioblend}"

test -z "$VIRTUAL_ENV" || deactivate || true
virtualenv .venv && . .venv/bin/activate
python -c 'import sys; sys.version_info >= (2, 7, 9) or sys.exit(1)' || pip install --upgrade --force-reinstall requests[security]
pip install --upgrade "$BIOBLEND_TARGET"
pip install ipython[all]
ipython notebook
