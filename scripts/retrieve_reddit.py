"""Retrieve Reddit citations through Reddit's public embed route."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "evidence" / "reddit"
DEST.mkdir(exist_ok=True)
sources = json.loads((ROOT / "data/rebuilt/sources.json").read_text())
results = []

for source in sources:
    url = source["url"]
    if "reddit.com/" not in url:
        continue
    parsed = urllib.parse.urlsplit(url)
    embed_url = urllib.parse.urlunsplit(("https", "embed.reddit.com", parsed.path, "", ""))
    result = {
        "source_id": source["source_id"],
        "original_url": url,
        "retrieval_url": embed_url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
    }
    try:
        request = urllib.request.Request(
            embed_url,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read()
            content_type = response.headers.get("Content-Type")
            if response.status != 200 or b"theme-embed" not in body[:1000]:
                raise ValueError("Response is not a Reddit embed page")
            path = DEST / f"{source['source_id']}.html"
            path.write_bytes(body)
            result.update(
                status="retrieved_pending_review",
                http_status=response.status,
                content_type=content_type,
                snapshot=str(path.relative_to(ROOT)),
                sha256=hashlib.sha256(body).hexdigest(),
            )
    except Exception as error:
        result.update(status="retrieval_error", error=str(error))
    results.append(result)
    time.sleep(0.5)

(DEST / "retrieval.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"Retrieved {sum(x['status'] == 'retrieved_pending_review' for x in results)} of {len(results)} Reddit posts")
