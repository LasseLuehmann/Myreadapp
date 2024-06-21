SET search_path TO project;

CREATE TYPE book_category_enum AS ENUM('programming', 'art', 'history', 'politics', 'other');
CREATE TYPE book_format_enum AS ENUM('ebook', 'hardcover');

CREATE TABLE book (
    isbn VARCHAR(13) PRIMARY KEY,
    title VARCHAR(50) NOT NULL, 
    description TEXT,
    page_count INT NOT NULL, 
    category book_category_enum NOT NULL, 
    published_date INT NOT NULL,
    publisher VARCHAR(50) NOT NULL, 
    authors VARCHAR(50) ARRAY NOT NULL,
    lang VARCHAR(50) NOT NULL,
    edition INT, 
    format book_format_enum NOT NULL
);

CREATE TABLE my_read(
    id SERIAL PRIMARY KEY,
    book_isbn VARCHAR(13) REFERENCES book(isbn),
    reader_username VARCHAR(50) REFERENCES reader(username),
    percentage_read INT DEFAULT 0,
    start_read_date DATE,
    end_read_date DATE,

    CHECK(percentage_read BETWEEN 0 AND 100),
    CHECK(end_read_date > start_read_date),

    CHECK((percentage_read = 0 AND start_read_date IS NULL) OR (percentage_read > 0 AND start_read_date IS NOT NULL)),
    CHECK((percentage_read = 100 AND end_read_date IS NOT NULL) OR (percentage_read < 100 AND end_read_date IS NULL))
);

CREATE TABLE reader(
    username VARCHAR(50) PRIMARY KEY,
    title VARCHAR(5),
    first_name VARCHAR(20),
    last_name VARCHAR(30) NOT NULL,

    CHECK(title IN ('Mrs', 'Mr', 'Ms', 'Dr'))
);

CREATE TABLE status_percent (
    id SERIAL PRIMARY KEY,
    percentage_read_range INT4RANGE,
    read_status VARCHAR(10),

    CHECK(read_status IN ('pending', 'reading', 'done'))
);

INSERT INTO status_percent(percentage_read_range, read_status)
VALUES ('[0,0]', 'pending'), ('[1,99]', 'reading'), ('[100,100]', 'done')