from bs4 import BeautifulSoup
import requests

# website url
url = "https://coinmarketcap.com/"
# send request and turn it into a text
result = requests.get(url).text
# reads the request
doc = BeautifulSoup(result, "html.parser")

# looks for tbody tag in the html
tbody = doc.tbody
# returns list of all the contents inside the tbody tag
trs = tbody.contents

# initialize dictionary
prices = {"Name": "   Prices"}
# iterates through the first 10 elements in trs
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    # saves the string inside the p tag
    fixed_name = name.p.string
    fixed_price = price.a.string

    # saves the fixed_name and fixed_price into the dictionary
    prices[fixed_name] = fixed_price

# iterates through the dictionary and prints the dictionary in a column format
# https://stackoverflow.com/questions/27067061/python-print-dictionary-using-column-formatting
for key, value in prices.items():
    print(f'{key:<4}    {value}')
