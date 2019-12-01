.SUFFIXES=
PY3=/usr/bin/env python3
SHELL=/bin/bash

.PHONY: all
all: install server

.PHONY: clean
clean:
	rm -rf venv

.PHONY: server
server: activate
	echo server

.PHONY: install
install: activate
	$(PY3) -m pip install -r requirements.txt

.PHONY: activate
activate: venv
	source venv/bin/activate

venv:
	$(PY3) -m virtualenv venv

