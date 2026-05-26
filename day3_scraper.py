import requests
from bs4 import BeautifulSoup
response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")
quotes = soup.find_all("div", class_="quote")
print(len(quotes))
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(text, "-", author)