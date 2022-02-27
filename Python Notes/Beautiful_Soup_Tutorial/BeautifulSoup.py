from bs4 import BeautifulSoup
import requests
import re

""" parsing html file"""

# opens the html file as file
# with open("/home/max/Python/Tutorials/index.html", "r") as file:
#     # {parameters} = {file_name, parser}
#     doc = BeautifulSoup(file, "html.parser")

# print(doc.prettify())

# tag = doc.title
# print(tag)

# # to access string in tag
# print(tag.string)

# # modify string insdie tag
# tag.string = "hello"
# print(tag.string)

# tags = doc.find_all("p")
# print(tags)

# access nested tags

# tags = doc.find_all("p")[0]
# print(tags.find_all("b"))


""" parsing website html """

# url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")
# # print(doc.prettify())

# # find price of gpu
# prices = doc.find_all(text="$")
# parent = prices[0].parent
# strong = parent.find("strong")
# print("$" + strong.string)


""" Searching for Tags and filtering """
with open("/home/max/Python/Tutorials/index2.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser")

# tag = doc.find("option")
# tag['selected'] = 'false'
# print(tag)

# see all attribuites
# print(tag.attrs)

# find a list of tags
# tags = doc.find_all(["p", "div", "li"])
# print(tags)

# find tag with the text undergraduate in it
# tags = doc.find_all(["option"], text="Undergraduate")
# print(tags)


# find specific attributes
# tags = doc.find_all(["option"], text="Undergraduate", value="undergraduat")
# print(tags)

# find different class names
# tags = doc.find_all(class_="btn-item")
# print(tags)

# look for characters after the $ symbol
# tags = doc.find_all(text=re.compile("\$.*"))
# for tag in tags:
#     print(tag.strip())


# limit number of results
# tags = doc.find_all(text=re.compile("\$.*"), limit=1)
# for tag in tags:
#     print(tag.strip())


# saving modification
# tags = doc.find_all("input", type="text")
# for tag in tags:
#     tag['placeholder'] = "I changed you!"

# with open("changed.html", "w") as file:
#     file.write(str(doc))


""" Navigating the HTML Tree """
url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody

trs = tbody.contents
# print(trs)

# tree sibling
# print(trs[0].next_sibling)
# print(trs[1].previous_sibling)

# tree parent and descendents
# print(trs[0].parent.name)
# print(list(trs[0].descendants))


# getting crypto prices
prices = {"Name": "   Prices"}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price


print(prices)
