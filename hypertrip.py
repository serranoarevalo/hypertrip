from utils import get_city_soup, get_country_soup, get_country_data, get_current_weather, format_names, get_currency_conversion, get_hotels


def hypertrip(city):
    city_soup = get_city_soup(format_names(city))

    country, country_soup = get_country_soup(city_soup)

    language, currency, currency_iso, timezone, iso_code = get_country_data(country_soup)

    current_weather = get_current_weather(country, city)

    one_dollar_is = get_currency_conversion('USD', currency_iso)

    hotels = get_hotels(iso_code, city.lower())

    return {
        'language': language,
        'currency': currency,
        'timezone': timezone,
        'weather': current_weather,
        'one_dollar_is': one_dollar_is,
        'hotels': hotels
    }