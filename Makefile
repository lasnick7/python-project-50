gendiff:
	uv run gendiff -h

install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist\hexlet_code-0.1.0-py3-none-any.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest


check:
	uv run ruff check gendiff
	uv run pytest