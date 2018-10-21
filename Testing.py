# Here we go testing a new functionality

from bs4 import BeautifulSoup

from HTMLReader.Interface import getPageDecodedContent
from HTMLReader.BasePostContentParser import BasePostContentParser
from MisteriumParser.GameClassParsers import BaseClassesParser

url = "http://misterium-rpg.ru/viewtopic.php?id=1572"

page = getPageDecodedContent(url)

# parser = BaseClassesParser()
parser = BasePostContentParser()
parser.feed(page)

print("=== HERE STARTS GATHERED INFO ===")
print(parser.show_posts_content())

# parser.showResultingContent()