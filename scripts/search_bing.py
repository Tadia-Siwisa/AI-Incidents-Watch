"""Small research helper for the environment's authorized Bing HTML route."""
import base64
import html
from html.parser import HTMLParser
import re
import sys
import urllib.parse
import urllib.request


class Results(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h2 = False
        self.current = None
        self.results = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h2":
            self.in_h2 = True
        elif tag == "a" and self.in_h2:
            self.current = {"href": attrs.get("href", ""), "title": []}

    def handle_data(self, data):
        if self.current is not None:
            self.current["title"].append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.current is not None:
            self.results.append(self.current)
            self.current = None
        elif tag == "h2":
            self.in_h2 = False


def unwrap(url):
    query = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
    value = query.get("u", [""])[0]
    if value.startswith("a1"):
        try:
            return base64.b64decode(value[2:] + "===").decode()
        except Exception:
            pass
    return url


for query in sys.argv[1:]:
    url = "https://www.bing.com/search?" + urllib.parse.urlencode({"q": query, "count": 10})
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode(errors="replace")
    parser = Results()
    parser.feed(body)
    print(f"QUERY: {query}")
    for item in parser.results[:10]:
        print("-", " ".join(item["title"]).strip(), "\n ", unwrap(html.unescape(item["href"])))
