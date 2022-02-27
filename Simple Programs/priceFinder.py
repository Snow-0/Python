# webscraping program that searches for gpu prices

from bs4 import BeautifulSoup
import requests
import re

search_term = input("What gpu do you want to search for? ")
url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
page = requests.get(url).text

# store gpu prices
items_found = {}

# parse the newegg page using Beautiful Soup
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong

# splitting string to grab the number on the right of the strong tag
# pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
pages = 1

# looks through all the pages that has the "3080" search term
for page in range(pages):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    # find the content inside the div tag
    div = doc.find(
        class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    # match any text that contains 3080, includes additional charcters not 3080
    items = div.find_all(text=re.compile(search_term))

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent['href']
        # find price of gpu
        next_parent = item.find_parent(class_="item-container")

        try:
            price = next_parent.find(
                class_="price-current").find("strong").string
            items_found[item] = {"price": int(
                price.replace(",", "")), "link": link}

        except:
            pass
# sorts item by the price
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

# prints out the dictionary
for item in sorted_items:
    # prints name
    print(item[0])
    # prints price
    print(f"${item[1]['price']}")
    # prints link of gpu
    print(item[1]['link'])
    print("--------------------")
