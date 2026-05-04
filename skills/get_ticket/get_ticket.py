"""
get_ticket — Claude Code agent tool

Fetches a GitHub Issue by number and returns structured ticket data.
"""

import json
import os
import requests
import sys
from pathlib import Path

OWNER = "vvsevolodovich"
REPO = "agent-one-tool-practice"
API_BASE = "https://api.github.com"
TICKETS_DIR = Path(__file__).parent.parent.parent / "data" / "tickets"


def _get_local(ticket_id: str) -> dict:
    ticket_path = TICKETS_DIR / f"{ticket_id}.json"
    if not ticket_path.exists():
        raise FileNotFoundError(f"Local ticket file not found: {ticket_path}")
    data = json.loads(ticket_path.read_text())
    comments = [
        c if isinstance(c, str) else c.get("body", "")
        for c in data.get("comments", [])
    ]
    return {
        "ticket_id": ticket_id,
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "comments": comments,
    }


def get_ticket(ticket_id: str) -> dict:
    """Fetch a GitHub issue and its comments, returning structured ticket data.

    Args:
        ticket_id: GitHub issue number (string or int).

    Returns:
        dict with keys: ticket_id, title, description, comments.
    """
    ticket_id = str(ticket_id).lstrip("#")
    token = os.environ.get("GITHUB_TOKEN")

    if not token:
        print("[get_ticket] No GITHUB_TOKEN found — reading from local JSON.", file=sys.stderr)
        return _get_local(ticket_id)

    headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {token}"}

    issue_url = f"{API_BASE}/repos/{OWNER}/{REPO}/issues/{ticket_id}"
    issue_resp = requests.get(issue_url, headers=headers)
    issue_resp.raise_for_status()
    issue = issue_resp.json()

    comments_url = f"{API_BASE}/repos/{OWNER}/{REPO}/issues/{ticket_id}/comments"
    comments_resp = requests.get(comments_url, headers=headers)
    comments_resp.raise_for_status()
    comments = [c["body"] for c in comments_resp.json()]

    return {
        "ticket_id": ticket_id,
        "title": issue["title"],
        "description": issue["body"] or "",
        "comments": comments,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_ticket.py <ticket_id>", file=sys.stderr)
        print("Example: python get_ticket.py 3", file=sys.stderr)
        sys.exit(1)

    result = get_ticket(sys.argv[1])
    print(json.dumps(result, indent=2))
