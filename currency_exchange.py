import datetime

import requests
from forex_python.converter import CurrencyRates
from other_files.constants import *

api_url = f"https://v6.exchangerate-api.com/v6/{exchangerate_key}/"
history_url = f"https://freecurrencyrates.com/en/exchange-rate-history/"
hist_url = f"https://api.currencyapi.com/v3/historical?apikey={currencyapi_key}"


def convert_currency(start_currency, end_currency, amount):
    pair_url = api_url + f"pair/{start_currency}/{end_currency}/{amount}"
    response_json = requests.get(pair_url).json()
    return response_json["conversion_result"]


def get_currency_info(currency):
    # Latest info of currency
    latest_url = api_url + f"latest/{currency}"
    response_json = requests.get(latest_url).json()
    return response_json["conversion_rates"]


def get_currency_history(start_currency, end_currency, year):
    c = CurrencyRates()
    date = datetime.datetime(year, 12, 31)
    response = c.get_rates(base_cur=start_currency, date_obj=date)
    return response[end_currency]


# def get_historical_info(start_currency, end_currency, year):
#     url = hist_url + f"&base_currency={start_currency}&currencies={end_currency}&date={year}-12-31 "
#
#     resp = requests.get(url)
#
#     return resp.json()["data"][end_currency]["value"]
#
#
# def get_currency_year_info(start_currency, end_currency, year):
#     # Self counting from currency site, but not work in pythonanywhere
#     historical_url = history_url + f"{start_currency}-{end_currency}/{year}/cbr"
#     page = requests.get(historical_url)
#     soup = BeautifulSoup(page.content, "html.parser")
#
#     year_mid = 0
#     num_list = soup.find_all("div", class_="one-month-data-rate")
#
#     length_list = len(num_list)
#     for num in num_list:
#         year_mid += float(str(num).split(">")[1].split("<")[0])
#
#     if length_list == 0:
#         raise ValueError("This year is not supported or error with currencies")
#     else:
#         return year_mid / length_list


if __name__ == '__main__':
    pass