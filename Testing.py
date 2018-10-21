# Here we go testing a new functionality

from HTMLReader.Interface import getPageDecodedContent
from HTMLReader.BasePostContentParser import BasePostContentParser
from MisteriumGameParsers.BasicParser import BasicParser

url = "http://misterium-rpg.ru/viewtopic.php?id=1572"

page = getPageDecodedContent(url)

# parser = BaseClassesParser()
parser = BasePostContentParser()
parser.feed(page)

#print("=== HERE STARTS GATHERED INFO ===")
#print(parser.show_posts_content())

textPrettifyParser = BasicParser()
for post in parser.get_posts():
    textPrettifyParser.process(post.get_content())

print("=== HERE STARTS GATHERED INFO ===")
textPrettifyParser.showResultingContent()