# Things CLI shortcuts

# Show tasks assigned to today
today:
    uv run things-cli today

# List all available tags
tags:
    uv run things-cli tags

# List undone tasks with a specific tag
tag TAG:
    uv run things-cli -t {{ TAG }} todos
