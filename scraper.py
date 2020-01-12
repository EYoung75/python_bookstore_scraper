import requests
from bs4 import BeautifulSoup
import pprint
import time

res = requests.get("http://books.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")
books = []
filtered = []
total_pages = 0

def get_all_pages():
    page=soup.find(class_="current")
    total_pages=page.string.strip()
    total_pages = int(total_pages[10:12])
    pprint.pprint(total_pages)

def get_titles():
    for link in soup.findAll("a"):
        title = link.get("title")
        if title is not None:
            books.append(title)
    pprint.pprint(books)

# def search():
#     _search_term = input()
#     for book in books:
#         if _search_term in book:
#             filtered.append(book)
#     pprint.pprint(filtered)

get_all_pages()




