"""
Exercise No. 236

Note: This exercise require basic knowledge of SQL.

sqlite3documentation: https://docs.python.org/3/library/sqlite3.html

Using sqlite3 package to manage SQLite databases, create a database named app.db.

The following SQL code creates a table named customer with columns: customer_id, first_name, last_name, and email.

    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        first_name  TEXT,
        last_name   TEXT,
        email       TEXT
    );

Using the above SQL code create the customer table in the app.db database. Then insert the following records into the
customer table using the executescript() method:

    ('John', 'Smith', 'john.smith@esmartdata.org')
    ('Joe', 'Doe', 'joe.doe@esmartdata.org')
    ('Mike', 'Smith', 'mike.smith@esmartdata.org')

Commit the changes and close the database connection. The tests run several test cases to validate the solution.
"""
import sqlite3


connection = sqlite3.connect('../Data/app.db')
cursor = connection.cursor()

query = ("""
    CREATE TABLE OR REPLACE customer (
        customer_id INTEGER PRIMARY KEY,
        first_name  TEXT,
        last_name   TEXT,
        email       TEXT
    );
""")
cursor.execute(query)

cursor.executescript("""
    INSERT INTO customer (first_name, last_name, email)
    VALUES ('John', 'Smith', 'john.smith@esmartdata.org'),
    ('Joe', 'Doe', 'joe.doe@esmartdata.org'),
    ('Mike', 'Smith', 'mike.smith@esmartdata.org');
""")

connection.commit()
connection.close()
