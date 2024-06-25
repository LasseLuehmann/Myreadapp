from typing import Optional
from src.db.queries import reader as reader_queries

class Reader:
    def __init__(self, username: str, title: str, first_name: str, last_name: str) -> None:
        self.username = username
        self.title = title
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def insert_data(cls, username: str, title: str, first_name: str, last_name: str) -> Optional['Reader']:
        reader: tuple[str] = reader_queries.insert_data(username, title, first_name, last_name)

        return cls(*reader) if reader else None
    
    @staticmethod
    def reader_has_done_at_least_one():
        reader = reader_queries.reader_has_done_at_least_one()
        return reader