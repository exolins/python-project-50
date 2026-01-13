install:
	uv sync

gendiff:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

lint-fix:
	uv run ruff check gendiff --fix

build:
	uv build
