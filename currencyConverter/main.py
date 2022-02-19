# Simple currency converter that uses the CurrencyConverter library and pandas for importing spreadsheets

from currency_converter import CurrencyConverter
import pandas
# import spreadsheet
xlsx = pandas.read_excel('~/Python/currencyConverter/currency.ods')
file = xlsx.to_dict("dict")

# list comphrension to get the columns of the currency name and the country and puts it in a list
abbrev_cur = [file["Abbreviation"][i]
              for i in file["Abbreviation"]]
full_name = [file["Name"][i] for i in file["Name"]]

# combine the list into a dictionary
dictionary = {abbrev_cur[i]: full_name[i] for i in range(len(abbrev_cur))}

# initualize converter object
converter = CurrencyConverter()

# always for the currency and country to be printed into the terminal


def print_dict():
    for key, value in dictionary.items():
        print(key, value)

# Main function


def currencyConverter():
    print_dict()
    # Asks for user input, though no input validation
    from_currency = input(
        "What currency are you converting from? ")
    to_currency = input(
        "What would you like to convert to? ")

    amount = input("Please input amount: ")
    # has user input as parameters for converter and rounds the total
    result = round(converter.convert(
        amount, from_currency, to_currency), 2)
    # print results
    print(str(result) + " " + to_currency)


currencyConverter()
