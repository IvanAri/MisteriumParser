import urllib.request
import re

url = "http://misterium-rpg.ru/viewtopic.php?id=1572"

BASIC_REQUESTER = urllib.request

# Здесь мы получаем сухую хтмл страницу
def getPage(url):
    requester = BASIC_REQUESTER
    return requester.urlopen(url).read()

# Немного грубой магии, но пока что сойдёт
def getPageCoding(rawPage):
    charsetPos = str(rawPage).find("charset=")
    coding = ""
    for c in range(charsetPos + 8, charsetPos + 30):
        symbol = str(rawPage)[c]
        if symbol != '"':
            coding += symbol
        else:
            break

    return coding

# Возвращает не отпаршеную, но декодированную страницу
def getPageDecodedContent(url):
    rawPage = getPage(url)
    coding = getPageCoding(rawPage)
    return rawPage.decode(coding)



