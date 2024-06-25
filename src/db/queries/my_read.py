from src.db.database import Database

def insert_data(book_isbn,reader_username,percentage_read,start_read_date):
    conn = Database()

    query = """
        INSERT INTO project.my_read(
            book_isbn,
            reader_username,
            percentage_read,
            start_read_date
        ) VALUES (%s,%s,%s,%s)
        RETURNING *;
    """

    with conn.cursor() as cursor:
        cursor.execute(query, (book_isbn,reader_username,percentage_read,start_read_date))
        my_read = cursor.fetchone()
        conn.commit()
        return my_read