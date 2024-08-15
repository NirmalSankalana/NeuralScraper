import requests
from bs4 import BeautifulSoup


def getPage(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


if __name__ == "__main__":
    URL = "https://odel.lk/women/casualwear/dresses/sc/3545"
    soup = getPage(URL)
    print(soup)
