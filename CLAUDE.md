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

This is a full-stack application with a Python backend and React frontend:

### Backend (Python)
- **Package Manager**: uv (modern Python package manager)
- **Build System**: Hatchling
- **Testing**: pytest
- **Linting**: ruff
- **Type Checking**: mypy
- **Python Version**: 3.13+
- **Runtime**: FastAPI (web framework)
- **Development**: mypy, pytest, ruff, pre-commit

### Frontend (React)
- **Framework**: React 19.1.0 with TypeScript
- **Build Tool**: Vite 7.0.4
- **UI Library**: React Bootstrap 2.10.10 + Bootstrap 5.3.7
- **API Client**: openapi-fetch 0.14.0
- **Type Checking**: TypeScript 5.8.3
- **Linting**: ESLint 9.30.1

#### Frontend Commands
- `npm run dev` - Start development server
- `npm run build` - Build for production (TypeScript compile + Vite build)
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build
- `npm run openapi` - Generate TypeScript types from OpenAPI spec at localhost:8000
- `npm run test:ts` - Type check without emitting files

### Code Organization

#### Backend
- `src/prai/` - Main package directory
- `src/prai/__init__.py` - Package initialization with main() function
- `src/prai/app.py` - Empty application file (likely for FastAPI app)

#### Frontend
- `frontend/src/` - React application source
- `frontend/src/components/` - React components (Navbar, Root, SinglePageApp)
- `frontend/src/types/` - TypeScript type definitions including API types
- `frontend/src/hooks/` - React hooks
- `frontend/dist/` - Built frontend assets

The project integrates a React frontend with a FastAPI backend. The frontend generates TypeScript types from the backend's OpenAPI specification.
