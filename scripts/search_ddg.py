"""Small research helper for the environment's authorized DuckDuckGo HTML route."""
from html.parser import HTMLParser
import sys
import time
import urllib.parse
import urllib.request


class Results(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current = None
        self.results = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "result__a" in attrs.get("class", "").split():
            self.current = {"url": attrs.get("href", ""), "title": []}

    def handle_data(self, data):
        if self.current is not None:
            self.current["title"].append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.current is not None:
            url = self.current["url"]
            query = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
            if "uddg" in query:
                url = query["uddg"][0]
            self.results.append((" ".join(self.current["title"]).strip(), url))
            self.current = None


for position, query in enumerate(sys.argv[1:]):
    if position:
        time.sleep(1)
    request = urllib.request.Request(
        "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query}),
        headers={"User-Agent": "Mozilla/5.0"},
    )
    print(f"QUERY: {query}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode(errors="replace")
    except Exception as error:
        print("- SEARCH ERROR:", error)
        continue
    parser = Results()
    parser.feed(body)
    for title, url in parser.results[:10]:
        print("-", title, "\n ", url)
