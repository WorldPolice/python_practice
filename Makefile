.PHONY: develop help lint test
.DEFAULT_GOAL := help

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

develop: ## install necessary packages to setup a dev environment
	pip install -r requirements.txt

lint: ## check style with flake8
	flake8 python_practice

test: ## run unit tests quickly with the default Python
	py.test tests