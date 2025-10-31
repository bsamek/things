# Things

This repository is for interacting with Things App.

## Prerequisites

This project uses `just` as a command runner and `uv` for Python package management.

**macOS:**
```bash
# Install just
brew install just

# Install uv
brew install uv
```

## Setup

After installing the prerequisites, install the Python dependencies:

```bash
# Create virtual environment and install packages
uv venv
uv pip install things-cli
```

## Available Commands

The justfile provides convenient shortcuts for common things-cli queries:

- `just today` - Show tasks assigned to today
- `just someday` - Show someday tasks
- `just tags` - List all available tags
- `just tag <TAG>` - List anytime tasks with a specific tag (excludes Someday tasks) (e.g., `just tag Computer` or `just tag "Read/Review"`)
- `just done <TAG>` - Show the last week's completed tasks with a specific tag grouped by day (e.g., `just done Office`)
- `just write` - Export Office-tagged tasks directly to the Obsidian note
