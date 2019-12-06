.SUFFIXES=
SHELL=/bin/bash
VENV=venv
PY3=/usr/bin/env python3
PY3V=source $(VENV)/bin/activate && $(PY3)
SOURCE_DIR=carboff

.PHONY: all
all:
	@echo "See README.md for installation"

.PHONY: clean
clean:
	rm -rf $(VENV)

.PHONY: format
format:
	$(PY3V) -m autopep8 --in-place --recursive --verbose $(SOURCE_DIR)

.PHONY: install-dev
install-dev: $(VENV)
	$(PY3V) -m pip install -e .[dev]

$(VENV):
	$(PY3) -m venv $(VENV)
