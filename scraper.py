import requests
from bs4 import BeautifulSoup
import pprint
import time


class Library():
    books = []
    def __init__(self):
        self.base_url = "http://books.toscrape.com/"
        self.get_books_on_page(2)
        self.search()


    def num_of_pages(self):
        soup=BeautifulSoup(requests.get(self.base_url).text, "html.parser")
        page=soup.find(class_="current")
        total_pages = int(page.string.strip()[10:12])
        return total_pages

    def get_books_on_page(self,int):
        soup = BeautifulSoup(requests.get(self.base_url+f"catalogue/page-{int}.html").text, "html.parser")
        for link in soup.findAll("a"):
            title = link.get("title")
            if title is not None:
                self.books.append(title)
        pprint.pprint(self.books)
        return self.books

    def get_all_books(self):
        for i in range(2):
            self.books.append(self.get_books_on_page(i))
        return self.books
            
    def search(self):
        _search_term = input("Search for a book: ")
        _filtered = [i for i in self.books if _search_term in i]
        pprint.pprint(_filtered)
        return _filtered
        

storefront = Library()




