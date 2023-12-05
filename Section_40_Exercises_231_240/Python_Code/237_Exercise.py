"""
Exercise No. 237

Note: This exercise require basic knowledge of SQL.

sqlite3documentation: https://docs.python.org/3/library/sqlite3.html

Using sqlite3 package to manage SQLite databases, a database called app.db was created. A table named customer was also
created in this database and several records were inserted:

    import sqlite3


    conn = sqlite3.connect('app.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        first_name  TEXT,
        last_name   TEXT,
        email       TEXT
    )''')

    cur.executescript('''INSERT INTO customer (first_name, last_name, email)
    VALUES ('John', 'Smith', 'john.smith@esmartdata.org');

    INSERT INTO customer (first_name, last_name, email)
    VALUES ('Joe', 'Doe', 'joe.doe@esmartdata.org');

    INSERT INTO customer (first_name, last_name, email)
    VALUES ('Mike', 'Smith', 'mike.smith@esmartdata.org');''')

    conn.commit()
    conn.close()

In the designated place, create a query that will extract the number of all records from the customer table and print it
to the console.

Expected result:

    3
"""
# Solution I
import sqlite3


conn = sqlite3.connect('../Data/app.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)''')

cur.executescript('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org');
 
INSERT INTO customer (first_name, last_name, email)
VALUES ('Joe', 'Doe', 'joe.doe@esmartdata.org');
 
INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Smith', 'mike.smith@esmartdata.org');''')

sql = '''SELECT COUNT(*) FROM customer'''
cur.execute(sql)
result = cur.fetchone()[0]
print(result)

conn.commit()
conn.close()


# Solution II
cur.execute('''SELECT COUNT(*) FROM customer''')
print(cur.fetchall()[0][0])
