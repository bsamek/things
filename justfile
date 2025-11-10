# Things CLI shortcuts

# Show tasks assigned to today
today:
    uv run things-cli -j today | uv run python group_by_project.py

# Show someday tasks
someday:
    uv run things-cli -j someday | uv run python group_by_project.py

# List all available tags
tags:
    uv run things-cli tags

# List undone tasks with a specific tag
tag TAG:
    uv run things-cli -t {{ TAG }} -j anytime | uv run python group_by_project.py

# Show inbox tasks
inbox:
    uv run things-cli -j inbox | uv run python group_by_project.py

# Show completed tasks from the last 7 days with a specific tag
done TAG:
    uv run things-cli -t {{ TAG }} -j logbook | uv run python logbook_last_week.py

# Show all available recipes
help:
    just --list

# Write Office-tagged tasks directly to Obsidian note
write:
    uv run things-cli -t Office -j anytime | uv run python group_by_project.py > '/Users/brian.samek/Google Drive/My Drive/Notes/To Do.md'
