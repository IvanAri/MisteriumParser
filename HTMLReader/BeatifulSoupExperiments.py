from bs4 import BeautifulSoup

from HTMLReader.Interface import getPageDecodedContent
from MisteriumGameParsers.GameClassParsers import BaseClassesParser

url = "http://misterium-rpg.ru/viewtopic.php?id=1572"

page = getPageDecodedContent(url)

soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
#print(soup.find_all("div", "post-content"))

parser = BaseClassesParser

for post in soup.find_all("div", "post-content"):
    # print(post)
    parser.feed(post)
    pass