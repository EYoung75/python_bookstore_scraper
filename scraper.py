import requests
from bs4 import BeautifulSoup
import pprint
import time

base_url = "http://books.toscrape.com/"
# res = requests.get("http://books.toscrape.com/")
# soup = BeautifulSoup(res.text, "html.parser")

def num_of_pages():
    soup=BeautifulSoup(requests.get(base_url).text, "html.parser")
    page=soup.find(class_="current")
    total_pages = int(page.string.strip()[10:12])
    return total_pages

def get_books_on_page(int):
    books = []
    soup = BeautifulSoup(requests.get(base_url+f"catalogue/page-{int}.html").text, "html.parser")
    for link in soup.findAll("a"):
        title = link.get("title")
        if title is not None:
            books.append(title)
    pprint.pprint(books)
    return books

def get_all_books():
    books = []
    for i in range(num_of_pages()):
        books.append(get_books_on_page(i))
    return books
        
# def search():
#     _search_term = input()
#     for book in books:
#         if _search_term in book:
#             filtered.append(book)
#     pprint.pprint(filtered)

pprint.pprint(get_all_books())




