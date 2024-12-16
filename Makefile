in:
	@uv run python ./get_input.py

pre:
	@uvx pre-commit run --all-files

test:
	@uv run pytest
