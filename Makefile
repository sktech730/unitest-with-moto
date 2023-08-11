PYTHON_ECR := public.ecr.aws/lambda/python:3.9
DOCKER_PLATFORM := linux/amd64

SHELL = /bin/bash

.PHONY: install-requirements, tests, venv

venv:
	python3 -m venv .venv

install-requirements:
	make venv
	pip install --upgrade -r requirements-test.txt

tests: install-requirements
	 coverage run -m pytest  && coverage report


define DOCKER_COMMAND
	docker run --user "$$(id -u):$$(id -g)" --rm \
	    --platform $(1) \
	    --volume $(2):/opt/project \
	    --workdir /opt/project \
	    --entrypoint pip \
	    $(3) \
	    $(4)
	cp -r $(5) dist
	git log -1 | head -n3 > dist/commit_manifest.txt
	( cd $(6) ; zip -9 -r $(2)/$(5).zip . )
endef
export DOCKER_COMMAND