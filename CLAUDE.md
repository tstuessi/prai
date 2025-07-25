# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This project uses [Task](https://taskfile.dev/) for build automation. Available commands:

- `task install` - Install dependencies using uv
- `task pre-commit` - Run pre-commit hooks on all files
- `task setup-pre-commit` - Setup pre-commit hooks
- `task serve` - Build frontend and run the FastAPI server locally with auto-reload
- `task test` - Run tests with pytest
- `task lint` - Run linting checks (ruff check)
- `task fix` - Run linting with auto-fix (ruff check --fix)
- `task check` - Run type checking (mypy)
- `task build` - Build frontend and copy to static folder

**Note**: `task serve` automatically runs `task build` first, so the frontend is always up-to-date when serving.

Direct uv commands:
- `uv sync` - Install/sync dependencies
- `uv run pytest` - Run tests
- `uv run ruff check --fix` - Lint and auto-fix code
- `uv run mypy src/prai` - Type check source code
- `uv run prai` - Run the main application

### Pre-commit Setup

This project uses pre-commit hooks to ensure code quality:

```bash
# Setup pre-commit hooks
task setup-pre-commit

# Run pre-commit on all files (optional)
task pre-commit
```

The pre-commit configuration runs:
- Standard hooks (trailing whitespace, end-of-file fixer, YAML/TOML validation, etc.)
- `task fix` - Auto-fix code with ruff
- `task check` - Type checking with mypy

## Project Structure

This is a Python package managed with uv and configured with modern Python tooling:

- **Package Manager**: uv (modern Python package manager)
- **Build System**: Hatchling
- **Testing**: pytest
- **Linting**: ruff
- **Type Checking**: mypy
- **Python Version**: 3.13+

### Dependencies
- **Runtime**: FastAPI (web framework)
- **Development**: mypy, pytest, ruff, pre-commit

### Code Organization
- `src/prai/` - Main package directory
- `src/prai/__init__.py` - Package initialization with main() function
- `src/prai/app.py` - Empty application file (likely for FastAPI app)

The project is in early development with minimal code structure. The main entry point is defined in `pyproject.toml` as `prai = "prai:main"`.
