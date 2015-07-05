#!/bin/sh

cd `dirname $0`

test -z "$VIRTUAL_ENV" || deactivate
virtualenv .venv && . .venv/bin/activate
python -c 'import sys; sys.version_info >= (2, 7, 9) or sys.exit(1)' || pip install --upgrade --force-reinstall requests[security]
pip install --upgrade bioblend
ipython notebook
