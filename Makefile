SHELL = /bin/bash

.PHONY: install-requirements, tests, venv, clean

venv:
	python3 -m venv .venv

install-requirements:
	make venv
	pip install --upgrade -r requirements-test.txt

tests: clean
	coverage run -m pytest  && coverage html



clean:
	rm -rf .pytest_cache/
	rm -f .coverage
	rm -rf htmlcov