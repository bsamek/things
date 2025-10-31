#!/usr/bin/env python3
"""Filter Things logbook entries to the past week and format as markdown."""

import json
import sys
from collections import OrderedDict
from datetime import date, datetime, timedelta
from typing import Iterable, List, Optional


def parse_stop_date(stop_date: str) -> Optional[datetime]:
    """Convert Things stop_date strings to datetime objects."""
    if not stop_date:
        return None
    try:
        # stop_date is stored as a localtime string, e.g. "2025-01-02 13:45:00"
        return datetime.fromisoformat(stop_date)
    except ValueError:
        return None


def filter_last_week(tasks: Iterable[dict]) -> "OrderedDict[str, List[str]]":
    """Group completed to-dos from the last 7 days by completion date."""
    today = date.today()
    cutoff = today - timedelta(days=6)

    grouped: "OrderedDict[str, List[str]]" = OrderedDict()

    for task in tasks:
        if task.get("type") != "to-do" or task.get("status") != "completed":
            continue

        stop = parse_stop_date(task.get("stop_date"))
        if not stop:
            continue

        stop_day = stop.date()
        if stop_day < cutoff or stop_day > today:
            continue

        day_key = stop_day.isoformat()
        grouped.setdefault(day_key, []).append(task.get("title", "").strip())

    return grouped


def print_markdown(grouped: "OrderedDict[str, List[str]]") -> None:
    """Print grouped tasks using markdown headings."""
    for day, titles in grouped.items():
        print(f"## {day}")
        for title in titles:
            if title:
                print(f"- {title}")
        print()


def main() -> None:
    """Format Things logbook JSON piped on stdin."""
    tasks = json.load(sys.stdin)
    if not isinstance(tasks, list):
        raise SystemExit("Expected list of tasks from things-cli JSON output.")

    grouped = filter_last_week(tasks)
    print_markdown(grouped)


if __name__ == "__main__":
    main()
