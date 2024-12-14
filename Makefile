in:
	@uv run python ./get_input.py

pre:
	@uv run pre-commit run --all-files

test:
	@uv run pytest
