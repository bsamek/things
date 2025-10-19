# Things CLI shortcuts

# Show tasks assigned to today
today:
    uv run things-cli today

# Show someday tasks
someday:
    uv run things-cli -j someday | uv run python group_by_project.py

# List all available tags
tags:
    uv run things-cli tags

# List undone tasks with a specific tag
tag TAG:
    uv run things-cli -t {{ TAG }} -j anytime | uv run python group_by_project.py
