
.PHONY: help test check

help:
	@echo make test - Run automated tests
	@echo make check - Run validation checks

test:
	set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 && python -m pytest -v test_validation.py

check:
	set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 && python -m pytest -v test_validation.py
	python -m compileall -q test_validation.py
