import re
import requests as requests
from bs4 import BeautifulSoup

base_url = 'https://sevenstars.nl/'
rest_path = 'professional/loadmore'
rest_url = base_url + rest_path
headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
myobj = {'type': '1', 'search': '', 'functiongroup': 'Testautomatiseerder', 'province': 'ALL', 'status': '0',
         'status': '1'}


def sanitize_string(in_text):
    return str(in_text.replace('\n', '')).strip()


def get_details_from_data(soup_data):
    all_the_divs = []
    for divs in soup_data.find_all("div", class_='site-container__inner'):
        for li in divs.find_all("div", recursive=False):
            span = li.find("span")
            if span:
                all_the_divs.append(sanitize_string(li.text))
    return all_the_divs


response = requests.post(rest_url, data=myobj, headers=headers)
data = response.json()
amount_of_vacancies = data['count']
if amount_of_vacancies > 0:
    pattern = '.*/vacature/(.*)\" class'
    result = re.match(pattern, data['html'])

    if result:
        detail_rest_url = base_url + 'partial/vacature/' + result.group(1)
        print('get the detail url ' + detail_rest_url)
        details_response = requests.get(detail_rest_url)
        details_data = details_response.json()
        details_data_html = details_data['html']
        soup = BeautifulSoup(details_data_html, 'html.parser')
        print(get_details_from_data(soup))
    else:
        print("I did not find any vacancies! " + data['html'])
