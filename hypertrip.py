from utils import get_city_soup, get_country_soup

city = "Seoul"  # input("Please write the name of the city you want to go to: ")

city_soup = get_city_soup(city)

country, country_soup = get_country_soup(city_soup)
