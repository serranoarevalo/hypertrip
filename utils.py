import requests
from bs4 import BeautifulSoup


wiki_url = "https://en.wikipedia.org/wiki/"
weather_url = "https://www.timeanddate.com/weather/"
currency_url = "https://www.x-rates.com/calculator/?"


def format_names(name):
    return name.replace(" ", "_")


def get_city_soup(name):
    wiki_request = requests.get(f'{wiki_url}{format_names(name)}')
    if wiki_request.status_code == 404:
        raise Exception("City Not Found")
    city_soup = BeautifulSoup(wiki_request.text, "html.parser")
    return city_soup


def get_country_soup(soup):
    info_box = soup.select_one("table.geography")
    country_link = info_box.find(text="Country")
    country = country_link.findNext("td").text
    country_request = requests.get(f'{wiki_url}{format_names(country)}')
    if country_request.status_code == 404:
        raise Exception("Country Not Found")
    country_soup = BeautifulSoup(country_request.text, "html.parser")
    name = country_soup.find("h1", {'id': "firstHeading"}).text
    return [name, country_soup]


def get_country_data(soup):
    info_box = soup.select_one("table", {'class': "geography"})
    language = info_box.select_one(".mergedtoprow", text="Official languages").find("td").find("a").text
    currency = info_box.find(text="Currency").findNext("td")
    currency_name, currency_iso = currency.findAll("a")
    iso_code = info_box.find(text="ISO 3166 code").findNext("td").text
    timezone = info_box.find(text="Time zone").findNext("td").text
    return [language, currency_name.text, currency_iso.text, timezone, iso_code]


def get_current_weather(country, city):
    formatted_country = country.replace(" ", "-").lower()
    formatted_city = city.replace(" ", "-").lower()
    weather_request = requests.get(f'{weather_url}{formatted_country}/{formatted_city}')
    weather_soup = BeautifulSoup(weather_request.text, "html.parser")
    temperature = weather_soup.find("div", text="Now").findNext("div", class_="h2").text
    return temperature


def get_currency_conversion(from_currency, to_currency):
    currency_request = requests.get(f'{currency_url}from={from_currency}&to={to_currency}&amount=1')
    currency_soup = BeautifulSoup(currency_request.text, "html.parser")
    output = currency_soup.find("span", {'class': "ccOutputRslt"}).text
    return output
