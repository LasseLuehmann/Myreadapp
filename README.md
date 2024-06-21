My Read App

This is a Command Line Application that helps keep track of readers and their reading engagement.
Database Mission Statement

The purpose of the My Read App Database is to maintain the data of our readers, and to supply information that supports the engagement of the reader.
Database Mission Objectives

    List title of all ebooks read by Dr
    How many books are there?
    How many readers are done reading at least one book?
    How many books do we have per category?
    How many books do we have per read status?

How to run

Before running this application, you should first setup the virtual environment, database, environment variables, install packages and optionally add fake data.
Set up database

NB: Open a terminal from the db folder in the working directory

-- Start psql shell from any database and superuser. Preferably postgres
psql -U postgres

-- Create the database 
CREATE DATABASE myreadapp;

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

Set up .env file

Create a .env file in the working directory. Copy the text below and change the values if yours is different.

db_host=localhost
db_name=myreadapp
db_user=postgres
db_password=postgres
db_port=5432

Set up Virtual Environment

In the working directory, open a terminal and run the following command

$ python3 -m venv .venv --prompt myreadapp

Source the virtual environment

$ source .venv/bin/activate

Install all packages

$ pip install -r requirements.txt

Start App

From the working directly, run the following command

$ python3 -m src.main

You will be presented with a menu. Continue by selecting the options you want.







