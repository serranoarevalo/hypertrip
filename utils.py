import requests
from bs4 import BeautifulSoup


wiki_url = "https://en.wikipedia.org/wiki/"


def format_names(name):
    return name.replace(" ", "_")


def get_city_soup(name):
    wiki_request = requests.get(f'{wiki_url}{format_names(name)}')
    if wiki_request.status_code == 404:
        raise Exception("City Not Found")
    city_soup = BeautifulSoup(wiki_request.text, "html.parser")
    return city_soup


def get_country_soup(soup):
    info_box = soup.select_one(".geography")
    country_link = info_box.find(text="Country")
    country = country_link.findNext("td").text
    country_request = requests.get(f'{wiki_url}{format_names(country)}')
    country_soup = BeautifulSoup(country_request.text, "html.parser")
    name = country_soup.find("h1", {'id': "firstHeading"}).text
    return [name, country_soup]
