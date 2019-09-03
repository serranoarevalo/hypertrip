from utils import get_city_soup, get_country_soup, get_country_data, get_current_weather, format_names, get_currency_conversion, get_hotels

city = format_names("Seoul")  # input("Please write the name of the city you want to go to: ")

city_soup = get_city_soup(city)

country, country_soup = get_country_soup(city_soup)

print(f'Gathering data for: {city}/{country}')

language, currency, currency_iso, timezone, iso_code = get_country_data(country_soup)

print(f'Language: {language}\nCurrency: {currency}\nTimezone: {timezone}\nCountry Code: {iso_code}')

current_weather = get_current_weather(country, city)

print(f'The weather is {current_weather}')

one_dollar_is = get_currency_conversion('USD', currency_iso)

print(f'1.00 USD = {one_dollar_is}')

hotels = get_hotels(iso_code, city.lower())

print(f'Top Rated Hotels:')

for hotel in hotels:
    print(hotel)