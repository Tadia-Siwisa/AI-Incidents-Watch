"""Retrieve cited URLs with TLS verification; log errors without treating them as refutations."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
import urllib.error

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'evidence'
DEST.mkdir(exist_ok=True)
sources=json.loads((ROOT/'data/rebuilt/sources.json').read_text())
def retrieve(source):
    result={**source,'retrieved_at':datetime.now(timezone.utc).isoformat(),'supports_claims':False}
    try:
        req=urllib.request.Request(source['url'],headers={'User-Agent':'AI-Incidents-Watch evidence research/0.1'})
        with urllib.request.urlopen(req,timeout=25) as response:
            body=response.read(20_000_001)
            if len(body)>20_000_000: raise ValueError('Response exceeded 20 MB; no complete snapshot saved')
            suffix='.pdf' if 'application/pdf' in response.headers.get('Content-Type','') else '.html'
            path=DEST/(source['source_id']+suffix)
            path.write_bytes(body)
            result.update(status='retrieved_pending_review',http_status=response.status,
                          final_url=response.url,content_type=response.headers.get('Content-Type'),
                          snapshot=str(path.relative_to(ROOT)),sha256=hashlib.sha256(body).hexdigest())
    except urllib.error.HTTPError as error:
        result.update(status='http_error',http_status=error.code,error=str(error))
    except Exception as error:
        message=str(error)
        result.update(status='network_policy_blocked' if 'Tunnel connection failed: 403' in message else 'retrieval_error',error=message)
    return result
results=list(ThreadPoolExecutor(max_workers=6).map(retrieve,sources))
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
(DEST/f'retrieval-{stamp}.json').write_text(json.dumps(results,indent=2)+'\n')
(DEST/'retrieval_latest.json').write_text(json.dumps(results,indent=2)+'\n')
from collections import Counter
print(dict(Counter(x['status'] for x in results)))
