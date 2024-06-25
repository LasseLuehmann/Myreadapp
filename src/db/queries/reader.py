from src.db.database import Database

# TODO: Query to insert reader
def insert_data(username: str, title: str, first_name: str, last_name: str) -> tuple[str]:
    conn = Database()

    query = """
        INSERT INTO project.reader(
            username,
            title,
            first_name,
            last_name
        ) VALUES(%s, %s, %s, %s)
        RETURNING *;
    """

    with conn.cursor() as cursor:
        cursor.execute(query, (username, title, first_name, last_name))
        reader = cursor.fetchone()
        conn.commit()
        return reader
    
def reader_has_done_at_least_one():
    conn = Database()

    query = """
        SELECT DISTINCT COUNT(*) 
        FROM project.my_read AS m
        JOIN project.status_percent AS s
            ON m.percentage_read <@ s.percentage_read_range
        WHERE s.read_status = 'done';
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        reader = cursor.fetchone()
        return reader