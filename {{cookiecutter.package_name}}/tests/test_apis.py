"""Test APIs."""
import importlib


def test_exposed():
    """Test package level exposed apis."""
    package = importlib.import_module('{{ cookiecutter.package_name }}')
    assert hasattr(package, '__version__')
    assert hasattr(package, '__author__')
