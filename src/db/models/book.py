from typing import Optional
from src.db.queries import book as book_queries


class Book:
    def __init__(
            self, 
            isbn, 
            title, 
            describtion,
            page_count,
            category,
            published_date,
            publisher,
            authors,
            lang,
            edition,
            format_
                 ):
        self.isbn = isbn
        self.title = title
        self.describtion = describtion
        self.page_count = page_count
        self.categoy = category
        self.published_date = published_date
        self.publisher = publisher
        self.authors = authors
        self.lang = lang
        self.edition = edition
        self.format = format_

    @classmethod
    def insert_data(cls,isbn,title,description,page_count,category,published_date,publisher,authors,lang,edition,format_):
        book = book_queries.insert_data(isbn,title,description,page_count,category,published_date,publisher,authors,lang,edition,format_)

        return cls(*book) if book else None

    @staticmethod
    def list_title_by_format_and_reader_title(format_: str, title: str):
        data = book_queries.list_title_by_format_and_reader_title(format_, title)
        result = [i[0] for i in data] 
        return result
    
    @staticmethod
    def amount_of_books():
        amount = book_queries.amount_of_books()
        return amount
    
    @staticmethod
    def amount_of_books_per_category():
        amount = book_queries.amount_of_books_per_category()
        return amount
    
    @staticmethod
    def amount_of_books_per_read_status():
        amount = book_queries.amount_of_books_per_read_status()
        return amount