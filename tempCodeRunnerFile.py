import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    with open("quotes.txt", "w", encoding="utf-8") as file:
        for i in range(1, 11):
            url = f"http://quotes.toscrape.com/page/{i}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_="quote")

            for quote in quotes:
                text = quote.find("span", class_="text").text
                author = quote.find("small", class_="author").text
                file.write(f"{text} - {author}\n\n")

            print(f"✅ Page {i} scraped!")

scrape_quotes()