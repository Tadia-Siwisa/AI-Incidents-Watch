"""Retrieve Reddit comments from the third-party PullPush archive.

These copies are useful for leads such as company replies, but remain archive
copies and must not be presented as direct Reddit retrieval.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "evidence" / "reddit" / "pullpush"
DEST.mkdir(exist_ok=True)
sources = json.loads((ROOT / "data/rebuilt/sources.json").read_text())
results = []

for source in sources:
    match = re.search(r"/comments/([a-z0-9]+)", source["url"])
    if not match:
        continue
    post_id = match.group(1)
    url = "https://api.pullpush.io/reddit/search/comment/?" + urllib.parse.urlencode(
        {"link_id": post_id, "size": 100}
    )
    result = {
        "source_id": source["source_id"],
        "post_id": post_id,
        "retrieval_url": url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
    }
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read()
            parsed = json.loads(body)
            if response.status != 200 or not isinstance(parsed.get("data"), list):
                raise ValueError("Response is not a PullPush comment result")
            path = DEST / f"{source['source_id']}.json"
            path.write_bytes(body)
            result.update(
                status="retrieved_archive_copy_pending_review",
                http_status=response.status,
                comment_count=len(parsed["data"]),
                snapshot=str(path.relative_to(ROOT)),
                sha256=hashlib.sha256(body).hexdigest(),
            )
    except Exception as error:
        result.update(status="retrieval_error", error=str(error))
    results.append(result)
    time.sleep(0.5)

(DEST / "retrieval.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"Retrieved archive comments for {sum(x['status'].startswith('retrieved') for x in results)} of {len(results)} posts")
