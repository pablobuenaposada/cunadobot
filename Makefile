PIP="venv/bin/pip"
PYTHON="venv/bin/python"

PIP_TMP=".venv_tmp/bin/pip"

PIP_TEST=".venv_test/bin/pip"
PYTHON_TEST=".venv_test/bin/python"
BLACK=".venv_test/bin/black"
ISORT=".venv_test/bin/isort"
FLAKE8=".venv_test/bin/flake8"


REQUIREMENTS:=requirements.txt
REQUIREMENTS_BASE:=requirements/base.txt
REQUIREMENTS_TEST:=requirements/test.txt

PIP_DOWNLOAD:=.pip_download

.PHONY: requirements settings

clean:
	@find . -name *.pyc -delete
	@rm -rf venv .venv_test .venv_tmp $(PIP_DOWNLOAD)

requirements:
	virtualenv -p python3.7 .venv_tmp
	$(PIP_TMP) install -U "pip"
	$(PIP_TMP) install -r $(REQUIREMENTS_BASE)
	$(PIP_TMP) freeze > requirements.txt
	@rm -rf .venv_tmp

virtualenv:
	test -d venv || virtualenv -p python3.7 venv
	$(PIP) install -U "pip"
	$(PIP) install -r $(REQUIREMENTS)

settings:
	@cp settings.example.py settings.py

install: virtualenv settings

virtualenv_test:
	test -d .venv_test || virtualenv -p python3.7 .venv_test
	$(PIP_TEST) install -U "pip"
	$(PIP_TEST) install -r $(REQUIREMENTS_TEST)

black-check: virtualenv_test
	$(BLACK) src tests --check

black:  virtualenv_test
	$(BLACK) src tests

isort-check: virtualenv_test
	$(ISORT) --diff cunao.py

isort: virtualenv_test
	$(ISORT) cunao.py

lint: virtualenv_test
	$(FLAKE8) cunao.py

test: virtualenv_test settings black-check isort-check lint
	$(PYTHON_TEST) -m pytest --cov=src tests

run: virtualenv
	$(PYTHON) cunao.py
