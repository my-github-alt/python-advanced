import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

alltheletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']


def dictify(div):
    result = {}
    for li in div.find_all("div", recursive=False):
        ul = li.find("span")
        if ul:
            key = ul.get('id')
            result[key] = li.text.replace('\n', '')
    return result


for letter in alltheletters:
    html_doc = requests.get('https://www.voedingswaardetabel.nl/voedingswaarde/' + letter + '/').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    for linkText in soup.find_all("div", id=re.compile('.*pnlRowContainer')):
        pprint(dictify(linkText))
