cookiecutter-pypackage-minimal
==============================

An opinionated, minimal [cookiecutter](https://github.com/audreyr/cookiecutter)
template for modern Python (Python 3) packages, and some guidelines for Python
packaging.

Philosophy
----------

The minimal package template is minimal in:
1. Minimal dependencies,
1. Minimal number of Python versions to support, and
1. Minimal efforts for packaging,

While testing and code quality should not be compromised.

Usage
-----

Get cookiecutter and create project template:

    pip install cookiecutter
    cookiecutter https://github.com/dawran6/cookiecutter-pypackage-minimal.git

Create virtual environment for the project. If you don't have a preferred way,
use Python3's built-in package `venv` to handle this. For example, create a
virtual environment called "env" and activate it:

    python3 -m venv env
    source env/bin/activate

Installed the required dependencies:

    pip install -r dev-requirements.txt

Now you can run tests:

    make test
    # for coverage report, use target test-cov:
    make test-cov

You should then change the classifiers in `{{ package_name }}/setup.py` - it is
assumed that the project will run on the modern Python (a.k.a. Python 3.)
You should adjust the classifiers that do apply to your package.
The full list of PyPI classifiers can be found
[here](https://pypi.python.org/pypi?:action=list_classifiers).

Fill out the README, and - if necessary - change the license to the project.

Explanation
-----------

The decisions `cookiecutter-pypackage-minimal` makes should all be explained here.

### README

* **README should use reStructuredText format**
  This is the format used by most Python tools, is expected by [setuptools]
  (https://setuptools.readthedocs.io), and can be used by
  [Sphinx](http://sphinx-doc.org/).
* **As few README files as possible**
  Additional README files (AUTHORS, CHANGELOG, etc) should be left to the user
  to create when necessary.

### `setup.py`

* **Use setuptools**
  It's the standard packaging library for Python. `distribute` has merged back
  into `setuptools`, and `distutils` is less capable.
* **setup.py should not import anything from the package**
  When installing from source, the user may not have the packages dependencies
  installed, and importing the package is likely to raise an `ImportError`.
* **setup.py should be the canonical source of package dependencies**
  There is no reason to duplicate dependency specifiers (i.e. also using a
  `requirements.txt` file). See the testing section below for testing dependencies.

### Testing

* **Uses [pytest](https://docs.pytest.org) as the default test runner**
  This can be changed easily, though pytest is a easier, more powerful test
  library and runner than the standard library's unittest.
* **Define testing dependencies in `tox.ini`**
  Avoid duplicating dependency definitions, and use `tox.ini` as the canonical
  description of how the unittests should be run.

Credits
-------

* Thanks to [kragniz](https://github.com/kragniz), most of the ideas are
  originated from kragniz's [cookiecutter-pypackage-minimal](https://github.com/kragniz/cookiecutter-pypackage-minimal)

