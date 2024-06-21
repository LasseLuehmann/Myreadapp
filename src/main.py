from src.db.models.reader import Reader
from src.db.models.book import Book
from typing import Optional

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
                    pass
                elif option == 3:
                    # TODO: INSERT MYREAD
                    pass
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
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    break
                elif option == 5:
                    pass
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