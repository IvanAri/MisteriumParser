# Here we go testing a new functionality

from HTMLReader.Interface import getPageDecodedContent
from HTMLReader.BasePostContentParser import BasePostContentParser
from MisteriumGameParsers.BasicParser import BasicParser
from MisteriumGameParsers.BaseClassParser import BaseClassParser

url = "http://misterium-rpg.ru/viewtopic.php?id=1572"

page = getPageDecodedContent(url)

# parser = BaseClassesParser()
parser = BasePostContentParser()
parser.feed(page)

#print("=== HERE STARTS GATHERED INFO ===")
#print(parser.show_posts_content())

textPrettifyParser = BasicParser()
posts = []
for post in parser.get_posts():
    textPrettifyParser.process(post.get_content())
    # textPrettifyParser.showResultingContent()
    posts.append(textPrettifyParser.getContentAndCleanUp())

baseClassParser = BaseClassParser()

print("=== HERE STARTS GATHERED INFO ===")
print(len(posts))
print(posts[28])
baseClassParser.process(posts[28])



