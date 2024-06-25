from src.db.database import Database

def insert_data(isbn,title,description,page_count,category,published_date,publisher,authors,lang,edition,format_):
    conn = Database()

    query = """
        INSERT INTO project.book(
            isbn,
            title,
            description,
            page_count,
            category,
            published_date,
            publisher,
            authors,
            lang,
            edition,
            format
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING *;
    """

    with conn.cursor() as cursor:
        cursor.execute(query, (isbn, title, description, page_count, category, published_date, publisher, authors, lang, edition, format_))
        book = cursor.fetchone()
        conn.commit()
        return book

def list_title_by_format_and_reader_title(format_: str, title: str):
    conn = Database()

    query = """
        SELECT DISTINCT b.title FROM project.book b
        JOIN project.my_read m ON b.isbn = m.book_isbn
        JOIN project.reader r ON m.reader_username = r.username
        WHERE r.title = %s AND b.format = %s;
    """

    with conn.cursor() as cursor:
        cursor.execute(query, (title, format_))
        list = cursor.fetchall()
        return list

def amount_of_books():
    conn = Database()

    query = """
        SELECT COUNT(*) FROM project.book;
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        amount = cursor.fetchone()
        return amount
    
def amount_of_books_per_category():
    conn = Database()

    query = """
        SELECT COUNT(*), category
        FROM project.book
        GROUP BY category;
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        amount = cursor.fetchall()
        return amount
    
def amount_of_books_per_read_status():
    conn = Database()

    query = """
        SELECT COUNT(b.*),s.read_status
        FROM project.book AS b
        JOIN project.my_read AS m
            ON b.isbn = m.book_isbn
        JOIN project.status_percent AS s
            ON m.percentage_read <@ s.percentage_read_range
        GROUP BY s.read_status;
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        amount = cursor.fetchall()
        return amount
    
