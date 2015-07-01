To install [BioBlend](http://bioblend.readthedocs.org) in the `~/.venv` virtualenv, open a terminal and execute the following commands:

```shell
$ cd
$ test -z "$VIRTUAL_ENV" && virtualenv .venv && . .venv/bin/activate
$ python -c 'import sys; sys.version_info >= (2, 7, 9) or sys.exit(1)' || pip install --upgrade --force-reinstall requests[security]
$ pip install bioblend
```
