#!/bin/sh

# Stop on problems.
set -e

cd "$(dirname "$0")"

test -z "$VIRTUAL_ENV" || deactivate || true
if [ ! -d .venv ]; then
    # If python is from Conda, make sure virtualenv comes from conda-forge
    if python3 -V 2>&1 | grep -q -e 'Anaconda' -e 'Continuum Analytics' || \
            python3 -c 'import sys; print(sys.version.replace("\n", " "))' | grep -q -e 'packaged by conda-forge' ; then
        conda install --yes --channel conda-forge 'virtualenv>=16'
    fi

    if ! command -v virtualenv >/dev/null; then
        echo "virtualenv not found, please install it."
        echo "For Debian/Ubuntu, this can be accomplished with:"
        echo ""
        echo "    sudo apt install virtualenv"
        exit 1
    fi

    virtualenv -p python3 .venv
fi
. .venv/bin/activate
pip install --upgrade -r requirements.txt
pip install jupyter
jupyter notebook
