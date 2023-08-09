PYTHON_ECR := public.ecr.aws/lambda/python:3.9
DOCKER_PLATFORM := linux/amd64

.PHONY: install-requirements, tests, venv

venv:
	python3 -m venv .venv

install-requirements:
	make venv
	pip install --upgrade -r requirements-test.txt

tests: install-requirements
	pytest .