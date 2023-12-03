.DEFAULT_GOAL := help
SHELL:=/bin/bash
export PROJECT_ROOT = $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# define the name of the virtual environment directory
VENV:=.venv

PYTHON=$(VENV)/bin/python3
PIP=$(VENV)/bin/pip

# targets which are NOT files
.PHONY: help venv run test clean

help:										## Shows the help
	@echo 'Usage: make <TARGETS>'
	@echo ''
	@echo 'Available targets are:'
	@echo ''
	@grep -E '^[ a-zA-Z_-]+:.*?## .*$$' $(shell echo "$(MAKEFILE_LIST)" | tr " " "\n" | sort -r | tr "\n" " ") \
		| sed 's/Makefile[a-zA-Z\.]*://' | sed 's/\.\.\///' | sed 's/.*\///' | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'
	@echo ''

# venv is a shortcut target
venv: $(VENV)/bin/activate                  ## Activate the venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: venv									## Execute python program
	$(PYTHON) main.py

test: venv									## Execute python tests
	$(PYTHON) -m unittest -v *_test.py

clean:										## Cleanup the artifacts
	rm -rf $(VENV) .mypy_cache
	find . -name __pycache__ | xargs rm -rf

#
# Usage: make VENV=my_venv run
#
