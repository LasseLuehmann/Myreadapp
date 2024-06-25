from src.db.models.reader import Reader
from src.db.models.book import Book
from src.db.models.my_read import MyRead
from typing import Optional
from datetime import datetime

class MenuDisplay:
    @staticmethod
    def display_main_menu():
        print("""
            WELCOME TO MY READ APP
              
              MENU
              -----------
              1. DATA MANIPULATION
              2. DATA QUERY
              00.QUIT              
        """)

    @staticmethod
    def display_DM_menu():
        print("""
            MENU -> DATA MANIPULATION

            1. INSERT READER
            2. INSERT BOOK
            3. INSERT MYREAD
            99. BACK
        """)

    @staticmethod
    def display_DQ_menu():
        print("""
            MENU -> DATA QUERY

            1. List title of a specific book format read by readers of a specific title
            2. How many books are there? # NO object
            3. How many readers are done reading at least one book? # readers
            4. How many books do we have per category? # books
            5. How many books do we have per read status? 
            99. Back
        """)

class DataInput():

    @staticmethod
    def input_for_reader_insert():
        username = input('Enter your username: ')
        title = input('Enter title (Mr, Mrs, Dr): ')
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')

        return {
            "username": username,
            "title": title,
            "first_name": first_name,
            "last_name": last_name 
        }
    
    @staticmethod
    def input_for_book_insert():
        isbn = input('Enter the isbn: ')
        title = input('Enter the title: ')
        description = input('Enter a describtion: ')
        page_count = int(input('Enter the page count: '))
        category = input('Enter a category: ')
        published_date = int(input('Enter the published year: '))
        publisher = input('Enter the publisher: ')
        authors = str({input('Enter the authors: ')})
        lang = input('Enter the language: ')
        edition = int(input('Enter the edition of the book: '))
        format_ = input('Enter the format (ebook,hardcover): ')

        return {
            "isbn": isbn,
            "title": title,
            "description": description,
            "page_count": page_count,
            "category": category,
            "published_date": published_date,
            "publisher": publisher,
            "authors": authors,
            "lang": lang,
            "edition": edition,
            "format_": format_
        }
    
    @staticmethod
    def input_for_my_read_insert():
        now = int(datetime.now().strftime('%Y'))
        book_isbn = input('Enter the isbn of the book: ')
        reader_username = input('Enter your username: ')
        percentage_read = 1
        start_read_date = now

        return {
            "book_isbn": book_isbn,
            "reader_username": reader_username,
            "percentage_read": percentage_read,
            "start_read_date": start_read_date
        }
    
    @staticmethod
    def input_for_DQ_option_one():
        format_ = input('Enter a format(ebook, hardcover): ')
        title = input('Enter title (Mr, Mrs, Dr): ')

        return {
            "format_": format_,
            "title": title
        }

def main():
    
    while True:
        MenuDisplay.display_main_menu()
        option: int = int(input('Choose an option to continue: '))

        if option == 1:
            # TODO: opertion for Manipulation
            while True:
                MenuDisplay.display_DM_menu()
                option: int = int(input('Choose an option to continue: '))

                if option == 1:
                    # TODO: INSERT READER
                    reader_detail: dict[str,str] = DataInput.input_for_reader_insert()
                    reader: Optional['Reader'] = Reader.insert_data(**reader_detail)

                    if reader:
                        print(f'Reader with username: {reader.username} inserted successfully')
                    else:
                        print('Insertion failed')                   
                elif option == 2:
                    # TODO: INSERT BOOK
                    book_detail = DataInput.input_for_book_insert()
                    book = Book.insert_data(**book_detail)

                    if book:
                        print(f'Book with title: {book.title} inserted successfully')
                    else:
                        print('Insertion failed')  
                elif option == 3:
                    # TODO: INSERT MYREAD
                    my_read_detail = DataInput.input_for_my_read_insert()
                    my_read = MyRead.insert_data(**my_read_detail)

                    if my_read:
                        print(f'My read was successfully inserted')
                    else:
                        print('Insertio failed')
                elif option == 99:
                    break
                else:
                    print('Option not recognized. Please, try again.')
        elif option == 2:
            # TODO: Operations for Query
            while True:
                MenuDisplay.display_DQ_menu()
                option: int = int(input('Choose an option to continue: '))

                if option == 1:
                    data = DataInput.input_for_DQ_option_one()
                    result = Book.list_title_by_format_and_reader_title(**data)
                    if result:
                        print('\nTitle\n','-'*20)
                        for title in result:
                            print(title)
                    else:
                        print('No data found')
                    
                    input('\nEnter to continue')

                elif option == 2:
                    result = Book.amount_of_books()
                    print(f'\nThere are {result[0]} books available.')
                    input('\nEnter to continue')
                elif option == 3:
                    result = Reader.reader_has_done_at_least_one()
                    print(f'{result[0]} readers had read at least one book completily.')
                    input('\nEnter to continue')
                elif option == 4:
                    result = Book.amount_of_books_per_category()
                    print('\namount\t|category\n','-'*20)
                    for i in result:
                        print(f'{i[0]}\t|{i[1]}')
                    input('\nEnter to continue')
                elif option == 5:
                    result = Book.amount_of_books_per_read_status()
                    print('\namount\t|readstatus\n','-'*20)
                    for i in result:
                        print(f'{i[0]}\t|{i[1]}')
                    input('\nEnter to continue')
                elif option == 99:
                    break
                else:
                    print('Option not recognized. Please, try again.')
        elif option == 0:
            print('Thanks for visiting.')
            break

        else:
            print('Option not recognized. Please, try again.')


if __name__ == '__main__':
    main()
