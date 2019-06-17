#!/bin/sh

# Stop on problems.
set -e

cd "$(dirname "$0")"

# Target git master using BIOBLEND_TARGET=git+git://github.com/galaxyproject/bioblend.git@master start_tutorial.sh
BIOBLEND_TARGET="${BIOBLEND_TARGET:-bioblend}"

test -z "$VIRTUAL_ENV" || deactivate || true
if [ ! -d .venv ]; then
    # If python is from Conda, make sure virtualenv comes from conda-forge
    if python -V 2>&1 | grep -q -e 'Anaconda' -e 'Continuum Analytics' || \
            python -c 'import sys; print(sys.version.replace("\n", " "))' | grep -q -e 'packaged by conda-forge' ; then
        conda install --yes --channel conda-forge 'virtualenv>=16'
    fi

    if ! command -v virtualenv >/dev/null; then
        echo "virtualenv not found, please install it."
        echo "For Debian/Ubuntu, this can be accomplished with:"
        echo ""
        echo "    sudo apt install virtualenv"
        exit 1
    fi

    virtualenv .venv
fi
. .venv/bin/activate
python -c 'import sys; sys.version_info >= (2, 7, 9) or sys.exit(1)' || pip install --upgrade --force-reinstall requests[security]
pip install --upgrade "$BIOBLEND_TARGET"
pip install jupyter
jupyter notebook
