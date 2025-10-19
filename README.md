# Things

This repository is for interacting with Things App.

## Prerequisites

This project uses `just` as a command runner. You need to install it first:

**macOS:**
```bash
brew install just
```

## Available Commands

The justfile provides convenient shortcuts for common things-cli queries:

- `just today` - Show tasks assigned to today
- `just someday` - Show someday tasks
- `just tags` - List all available tags
- `just tag <TAG>` - List anytime tasks with a specific tag (excludes Someday tasks) (e.g., `just tag Computer` or `just tag "Read/Review"`)
