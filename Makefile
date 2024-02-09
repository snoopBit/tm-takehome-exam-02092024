include .env
.PHONY: build

build: venv requirements.txt
	venv/bin/pip-sync requirements.txt

venv:
	python3 -m venv venv
	venv/bin/pip3 install pip-tools wheel twine

requirements.txt: requirements.in
	venv/bin/pip-compile -o requirements.txt requirements.in --allow-unsafe --resolver=backtracking

dagit: build
	venv/bin/dagit -h 0.0.0.0

daemon:
	venv/bin/dagster-daemon run