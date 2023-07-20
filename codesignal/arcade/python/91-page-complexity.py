from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.depth = 0
        self.max_depth = 0
        self.deepest_tags = set()
        self.tags_at_current_depth = set()

    def handle_starttag(self, tag, attrs):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth
            self.deepest_tags = {tag}
        elif self.depth == self.max_depth:
            self.deepest_tags.add(tag)
        self.tags_at_current_depth.add(tag)

    def handle_endtag(self, tag):
        if tag in self.tags_at_current_depth:
            self.tags_at_current_depth.remove(tag)
        if self.depth == self.max_depth and not self.tags_at_current_depth:
            self.max_depth -= 1
        self.depth -= 1

def solution(document):
    parser = MyHTMLParser()
    parser.feed(document)
    return sorted(list(parser.deepest_tags))