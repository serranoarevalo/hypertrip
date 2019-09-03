from utils import get_city_soup, get_country_soup, get_country_data, get_current_weather, format_names

city = format_names("Seoul")  # input("Please write the name of the city you want to go to: ")

city_soup = get_city_soup(city)

country, country_soup = get_country_soup(city_soup)

print(f'Gathering data for: {city}/{country}')

language, currency, currency_iso, timezone, iso_code = get_country_data(country_soup)

print(f'Language: {language}, Currency: {currency}, Timezone: {timezone}, Country Code: {iso_code}')


current_weather = get_current_weather(country, city)