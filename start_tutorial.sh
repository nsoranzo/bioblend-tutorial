#!/bin/sh

# Stop on problems.
set -e

cd "$(dirname "$0")"

# Deactivate current virtual environment
test -z "$VIRTUAL_ENV" || deactivate || true

if ! command -v python3 >/dev/null; then
    echo "python3 not found, please install it"
    exit 1
fi

if [ ! -d .venv ]; then
    # First try to use the venv standard library module, although it is not
    # always installed by default on Linux distributions.
    if ! python3 -m venv .venv; then
        echo "Creating the Python virtual environment using the venv standard library module failed."
        echo "Trying with virtualenv now."
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
fi

. .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install --upgrade -r requirements.txt
pip install jupyterlab
jupyter-lab
