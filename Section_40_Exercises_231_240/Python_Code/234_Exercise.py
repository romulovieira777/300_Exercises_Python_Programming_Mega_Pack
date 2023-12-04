"""
Exercise No. 234

Note: This exercise require basic knowledge of SQL.

sqlite3documentation: https://docs.python.org/3/library/sqlite3.html

Using sqlite3 package to manage SQLite databases, create a database named app.db.

The following SQL code creates a table customer with columns: customer_id, first_name, last_name, and email.

    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        first_name  TEXT,
        last_name   TEXT,
        email       TEXT
    );

Using the above SQL code create the customer table in the app.db database. Then insert the following record into the
customer table:

    (1, 'John', 'Smith', 'john.smith@esmartdata.org')

Commit the changes and close the database connection. The tests run several test cases to validate the solution.
"""
import sqlite3


connection = sqlite3.connect('../Data/app.db')
cursor = connection.cursor()

query = ("""
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        first_name  TEXT,
        last_name   TEXT,
        email       TEXT
    );
""")
cursor.execute(query)

cursor.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org')''')

connection.commit()
connection.close()
