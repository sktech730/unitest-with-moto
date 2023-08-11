SHELL = /bin/bash

.PHONY: install-requirements, tests, venv

venv:
	python3 -m venv .venv

install-requirements:
	make venv
	pip install --upgrade -r requirements-test.txt

tests:
	 coverage run -m pytest  && coverage report