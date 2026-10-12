
.PHONY: help test check

help:
	@echo make test - Run automated tests
	@echo make check - Run validation checks

test:
	python -m pytest -v test_validation.py

check:
	python -m pytest -v test_validation.py
	python -m compileall -q test_validation.py
