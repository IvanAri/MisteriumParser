from Lib.html import parser

LIB_PARSER = parser.HTMLParser

class BasePostContentParser(LIB_PARSER):

    def __init__(self):
        super(BasePostContentParser, self).__init__()

        self.isPostContentEncountered = False

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag %s with attrs %s:" % (tag, attrs))
        if ("class", "post-content") in attrs:
            print("Found post-content")
            self.isPostContentEncountered = True

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        if tag == "div" and self.isPostContentEncountered:
            self.isPostContentEncountered = False

    def handle_data(self, data):
        if self.isPostContentEncountered:
            print("Encountered data :", data)
        pass


