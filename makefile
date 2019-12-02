.SUFFIXES=
SHELL=/bin/bash
VENV=venv
PY3=/usr/bin/env python3
PY3V=source $(VENV)/bin/activate && $(PY3)
SOURCE_DIR=carboff

.PHONY: all
all: install server

.PHONY: clean
clean:
	rm -rf venv

.PHONY: format
format:
	$(PY3V) -m autopep8 --in-place --recursive --verbose $(SOURCE_DIR)

.PHONY: server
server:
	$(PY3V) $(SOURCE_DIR)/server.py $(args)

.PHONY: install
install: venv
	$(PY3V) -m pip install -r requirements.txt

venv:
	$(PY3) -m virtualenv venv
