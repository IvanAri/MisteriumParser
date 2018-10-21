from Lib.html import parser
from RawHTMLParser.UtilityClasses import PostContent

LIB_PARSER = parser.HTMLParser

class BasePostContentParser(LIB_PARSER):

    def __init__(self):
        super(BasePostContentParser, self).__init__()
        self.posts = [] # list of PostContent objects
        self.postIndex = 0
        self.isPostContentEncountered = False

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag %s with attrs %s:" % (tag, attrs))
        if ("class", "post-content") in attrs:
            print("Found post-content")
            self.isPostContentEncountered = True
            newPost = PostContent()
            self.posts.append(newPost)

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        if tag == "div" and self.isPostContentEncountered:
            self.isPostContentEncountered = False
            self.postIndex += 1

    def handle_data(self, data):
        if self.isPostContentEncountered:
            # print("Encountered data :", data)
            index = self.postIndex
            self.posts[index].add_line(data.strip())
        pass

    def get_posts(self):
        return self.posts

    def show_posts_content(self):
        for post in self.posts:
            post.show()

