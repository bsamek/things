# Things CLI shortcuts

# Show tasks assigned to today
today:
    uv run things-cli today

# Show someday tasks
someday:
    uv run things-cli someday

# List all available tags
tags:
    uv run things-cli tags

# List undone tasks with a specific tag
tag TAG:
    uv run things-cli -t {{ TAG }} anytime
