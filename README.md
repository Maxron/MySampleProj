# MySampleProj

A sample project for python to description python package.

## Getting start

### Environment request
- python 3.6+
- [pipenv](https://github.com/pypa/pipenv)

### Install depencies
```bash
$ pipenv install
```

### Run task
Use _make_ command for task running

#### All
Default action, same as [Build](#Build)
```bash
$ make
```

#### Build
Run the command `python setup.py sdist bdist_wheel bdist_egg` 
```bash
$ make build
```

#### install
Run the command `pip install {target}.tar.gz`, the target file is built after `make`
```bash
$ make install
```

#### demo
Run the command `demo_wei` after install
```bash
$ make demo
```
#### clean
Delete the output files and folders after run `make` or `make build`
```bash
$ make clean
```