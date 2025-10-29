#!/usr/bin/env python3
"""Group Things tasks by project/area and output with markdown headers."""

import json
import sys
from collections import defaultdict

def main():
    # Read JSON from stdin
    data = json.load(sys.stdin)

    # Group tasks by project or area
    grouped = defaultdict(list)

    for item in data:
        # Skip if this is a project item rather than a to-do
        if item.get("type") != "to-do":
            continue

        title = item.get("title", "")
        status = item.get("status", "")

        # Prefer project_title, fall back to area_title
        group_name = item.get("project_title") or item.get("area_title") or "No Project"

        grouped[group_name].append(
            {
                "title": title,
                "status": status,
            }
        )

    # Sort groups alphabetically and output
    for group_name in sorted(grouped.keys()):
        print(f"# {group_name}")
        for task in grouped[group_name]:
            checkbox = "x" if task["status"] == "completed" else " "
            print(f"- [{checkbox}] {task['title']}")
        print()  # Blank line between sections

if __name__ == "__main__":
    main()
