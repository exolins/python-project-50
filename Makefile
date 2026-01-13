install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml


package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

check: test lint
	
lint-fix:
	uv run ruff check gendiff --fix

build:
	uv build
