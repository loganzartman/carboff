.SUFFIXES=
PY3=/usr/bin/env python3
SHELL=/bin/bash

.PHONY: all
all: install server

.PHONY: clean
clean:
	rm -rf venv

.PHONY: server
server:
	source venv/bin/activate && \
	$(PY3) server.py $(args)

.PHONY: install
install: venv
	source venv/bin/activate && \
	$(PY3) -m pip install -r requirements.txt

venv:
	$(PY3) -m virtualenv venv

