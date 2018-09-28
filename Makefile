PIP="venv/bin/pip"
PYTHON="venv/bin/python"

PIP_TMP=".venv_tmp/bin/pip"

PIP_TEST=".venv_test/bin/pip"
ISORT=".venv_test/bin/isort"
FLAKE8=".venv_test/bin/flake8"

REQUIREMENTS:=requirements.txt
REQUIREMENTS_BASE:=requirements/base.txt
REQUIREMENTS_TEST:=requirements/test.txt

PIP_DOWNLOAD:=.pip_download

.PHONY: requirements

clean:
	@find . -name *.pyc -delete
	@rm -rf venv .venv_test .venv_tmp $(PIP_DOWNLOAD)

requirements:
	virtualenv -p python3.6 .venv_tmp
	$(PIP_TMP) install -U "pip"
	$(PIP_TMP) install -r $(REQUIREMENTS_BASE)
	$(PIP_TMP) freeze > requirements.txt
	@rm -rf .venv_tmp

virtualenv:
	test -d venv || virtualenv -p python3.6 venv
	$(PIP) install -U "pip"
	$(PIP) install -r $(REQUIREMENTS)

install: virtualenv
	@cp settings.example.py settings.py

virtualenv_test:
	test -d .venv_test || virtualenv -p python3.6 .venv_test
	$(PIP_TEST) install -U "pip"
	$(PIP_TEST) install -r $(REQUIREMENTS_TEST)

isort-check: virtualenv_test
	$(ISORT) --diff cunao.py

isort: virtualenv_test
	$(ISORT) cunao.py

lint: virtualenv_test
	$(FLAKE8) cunao.py

test: virtualenv_test isort-check lint

run: virtualenv
	$(PYTHON) cunao.py
