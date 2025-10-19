# Things

This repository is for interacting with Things App.

## Available Commands

The justfile provides convenient shortcuts for common things-cli queries:

- `just today` - Show tasks assigned to today
- `just tags` - List all available tags
- `just tag <TAG>` - List anytime tasks with a specific tag (excludes Someday tasks) (e.g., `just tag Computer` or `just tag "Read/Review"`)
