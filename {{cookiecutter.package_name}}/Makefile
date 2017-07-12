build:
	python setup.py sdist --formats=gztar,zip
	python setup.py bdist_wheel --universal

clean-pyc:
	find {{ cookiecutter.package_name }} -name '*.pyc' -exec rm -f {} +
	find {{ cookiecutter.package_name }} -name '*.pyo' -exec rm -f {} +
	find {{ cookiecutter.package_name }} -name '*~' -exec rm -f {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

lint:
	flake8 {{ cookiecutter.package_name }}/ tests/

test: clean-pyc
	py.test --verbose --color=yes tests/

test-cov: clean-pyc
	py.test --verbose --color=yes --cov={{ cookiecutter.package_name }} --cov-report html tests/