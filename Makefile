.PHONY: help test run pre-commit install clean

help:
	@echo "Profundus MCP Forge - Available targets:"
	@echo "  make test         - Run local smoke test (recommended before push)"
	@echo "  make run          - Start the server locally"
	@echo "  make pre-commit   - Install and run pre-commit hooks"
	@echo "  make install      - Install dependencies + pre-commit"
	@echo "  make clean        - Remove cache files"

install:
	pip install -r requirements.txt
	pip install pre-commit
	pre-commit install

pre-commit:
	pre-commit run --all-files

test:
	python scripts/test_local.py

run:
	python -m servers.python.main

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Cleaned cache files"