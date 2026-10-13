#!/usr/bin/env python3
"""Run a discovery-only delta scan for possible AI-agent incident evidence.

This script collects candidates. It never changes an adjudicated finding or the
46-family baseline. A human/source review must decide which candidates belong in
the dated evidence-update JSON and workbook.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
WATCH = ROOT / "data/monitoring/case_watch_2026-10-13.json"
STATE = ROOT / "data/monitoring/radar_state.json"
USER_AGENT = "Mozilla/5.0 AI-Incident-Watch evidence radar"

BROAD_NEWS_QUERIES = [
    '"AI agent" (deleted OR accessed OR submitted OR hacked OR unauthorized OR unintended)',
    '(Claude OR ChatGPT OR Gemini OR Cursor OR Replit) agent incident',
    '"AI agent" (database OR files OR drive OR credentials OR government)',
    '"rogue AI agent"',
]
REDDIT_QUERIES = [
    "Claude deleted",
    "Cursor deleted",
    "Gemini deleted",
    "Replit database",
    "coding agent wiped",
    "AI agent unauthorized",
    "agent stuck loop cost",
]


def get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read())


def google_news(query: str) -> list[dict]:
    encoded = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded}&hl=en-US&gl=US&ceid=US:en"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        root = ET.fromstring(response.read())
    rows = []
    for item in root.findall("./channel/item"):
        source = item.find("source")
        rows.append({
            "title": item.findtext("title"),
            "published": item.findtext("pubDate"),
            "google_news_url": item.findtext("link"),
            "source": source.text if source is not None else None,
            "source_url": source.attrib.get("url") if source is not None else None,
        })
    return rows


def pullpush(query: str, after_epoch: int) -> list[dict]:
    params = urllib.parse.urlencode({
        "q": query,
        "after": after_epoch,
        "size": 100,
        "sort": "desc",
        "sort_type": "created_utc",
    })
    payload = get_json(f"https://api.pullpush.io/reddit/search/submission/?{params}")
    rows = []
    for item in payload.get("data", []):
        rows.append({
            "id": item.get("id"),
            "created_utc": item.get("created_utc"),
            "subreddit": item.get("subreddit"),
            "author": item.get("author"),
            "title": item.get("title"),
            "selftext": item.get("selftext"),
            "url": item.get("url") or ("https://www.reddit.com" + item.get("permalink", "")),
        })
    return rows


def replace_after(query: str, since: str) -> str:
    query = re.sub(r"\s+after:\d{4}-\d{2}-\d{2}\b", "", query)
    return f"{query} after:{since}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", help="Exclusive lower date, YYYY-MM-DD")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="Run label, YYYY-MM-DD")
    args = parser.parse_args()

    state = json.loads(STATE.read_text()) if STATE.exists() else {"last_adjudicated": "2026-10-09"}
    since = args.since or state["last_adjudicated"]
    since_dt = datetime.fromisoformat(since).replace(tzinfo=timezone.utc)
    after_epoch = int(since_dt.timestamp())
    watched = json.loads(WATCH.read_text())["cases"]

    case_results = []
    for case in watched:
        query = replace_after(case["query"], since)
        try:
            results = google_news(query)
            error = None
        except Exception as exc:  # Keep partial discovery output for diagnosis.
            results = []
            error = repr(exc)
        case_results.append({
            "case_id": case["case_id"], "title": case["title"],
            "query": query, "results": results, "error": error,
        })

    broad_results = []
    for base_query in BROAD_NEWS_QUERIES:
        query = f"{base_query} after:{since}"
        try:
            results = google_news(query)
            error = None
        except Exception as exc:
            results = []
            error = repr(exc)
        broad_results.append({"query": query, "results": results, "error": error})

    reddit_by_id = {}
    reddit_errors = []
    for query in REDDIT_QUERIES:
        try:
            for row in pullpush(query, after_epoch):
                reddit_by_id[row["id"]] = {**row, "matched_query": query}
        except Exception as exc:
            reddit_errors.append({"query": query, "error": repr(exc)})

    payload = {
        "metadata": {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "since_exclusive": since,
            "as_of": args.as_of,
            "status": "discovery_only_not_adjudicated",
            "notice": "Headlines and posts are leads, not evidence findings. Open relevant passages and preserve corrections before changing the corpus.",
        },
        "case_queries": case_results,
        "broad_news_queries": broad_results,
        "reddit_candidates": sorted(reddit_by_id.values(), key=lambda x: x.get("created_utc") or 0, reverse=True),
        "reddit_errors": reddit_errors,
    }
    dest = ROOT / "data/monitoring/raw" / args.as_of / "radar_discovery.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(
        f"Saved {dest.relative_to(ROOT)}: {len(case_results)} case queries, "
        f"{sum(len(x['results']) for x in broad_results)} broad-news hits, "
        f"{len(reddit_by_id)} deduplicated Reddit candidates."
    )


if __name__ == "__main__":
    main()
