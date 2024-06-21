-- Connect to the database
\c myreadapp

-- Create the schema 'project'
CREATE SCHEMA project;

-- Run the script to create all tables
--- NB: This will insert standard values in the read_status table
------ Please, check it and adjust according to need
\i create_tables.sql

-- OPTIONAL: Insert dummy data to start with 
\i reader.sql   -- insert reader data
\i book.sql     -- insert book data
\i my_read.sql  -- insert my read data
```
### Set up .env file
Create a `.env` file in the working directory. Copy the text below and change the values if yours is different.

```
db_host=localhost
db_name=myreadapp
db_user=postgres
db_password=postgres
db_port=5432
```

### Set up Virtual Environment
In the working directory, open a terminal and run the following command

```bash
$ python3 -m venv .venv --prompt myreadapp
```
Source the virtual environment

```bash
$ source .venv/bin/activate
```
Install all packages

```bash
$ pip install -r requirements.txt
```

### Start App
From the working directly, run the following command
```bash
$ python3 -m src.main
```
You will be presented with a menu. Continue by selecting the options you want.











Message codes









