from typing import List
import re
from pprint import pprint
from string import ascii_lowercase as alltheletters
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup, Tag


def dictify(div: Tag) -> dict:
    result = {}
    for li in div.find_all("div", recursive=False):
        if ul := li.find("span"):
            key = ul.get('id')
            result[key] = str(li.text).strip()
    return result


def voedingswaardes(letter: str) -> List[dict]:
    html_doc = requests.get(f'https://www.voedingswaardetabel.nl/voedingswaarde/{letter}/').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    map_iter = map(dictify, soup.find_all("div", id=re.compile('.*pnlRowContainer')))
    return list(map_iter)
if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        # result -> Iterator[List[dict]]
        iter_of_list_dicts = executor.map(voedingswaardes, alltheletters)
    for list_dicts, letter in zip(iter_of_list_dicts, alltheletters):
        # print(f'Webpage: {letter} bevat {len(list_dicts)} producten')
        for dicts in list_dicts:
            pprint(dicts)
