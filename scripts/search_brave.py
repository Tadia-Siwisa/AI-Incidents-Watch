"""Small research helper for the environment's authorized Brave Search HTML route."""
from html.parser import HTMLParser
import sys
import time
import urllib.parse
import urllib.request


class Results(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "a" and "l1" in classes and attrs.get("href", "").startswith("http"):
            self.results.append((attrs.get("title", ""), attrs["href"]))


for position, query in enumerate(sys.argv[1:]):
    if position:
        time.sleep(3)
    url = "https://search.brave.com/search?" + urllib.parse.urlencode({"q": query})
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode(errors="replace")
    except Exception as error:
        print(f"QUERY: {query}\n- SEARCH ERROR: {error}")
        continue
    parser = Results()
    parser.feed(body)
    print(f"QUERY: {query}")
    seen = set()
    for title, result_url in parser.results:
        if result_url in seen:
            continue
        seen.add(result_url)
        print("-", title, "\n ", result_url)
        if len(seen) == 10:
            break
