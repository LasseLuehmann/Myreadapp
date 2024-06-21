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

    @staticmethod
    def list_title_by_format_and_reader_title(format_: str, title: str):
        data = book_queries.list_title_by_format_and_reader_title(format_, title)
        result = [i[0] for i in data] 
        return result