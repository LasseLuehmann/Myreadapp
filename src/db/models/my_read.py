from typing import Optional
from src.db.queries import my_read as my_read_queries

class MyRead:

    def __init__(
            self,
            id,
            book_isbn,
            reader_username,
            pecentage_read,
            start_read_date,
            end_read_date
    ):
        self.book_isbn = book_isbn
        self.id = id
        self.reader_username = reader_username
        self.percentage_read = pecentage_read
        self.start_read_date = start_read_date
        self.end_read_date = end_read_date

    @classmethod
    def insert_data(cls,book_isbn,reader_username,percentage_read,start_read_date):
        my_read = my_read_queries.insert_data(book_isbn,reader_username,percentage_read,start_read_date)

        return cls(*my_read) if my_read else None