"""
Exercise No. 243

Note: This exercise require basic knowledge of SQL.

sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html

csv documentation: https://docs.python.org/3/library/csv.html

The file Product.csv (utf-8 encoding) containing data about products in a creation warehouse is attached to the exercise.
In this exercise, you will create a SQLite database (named store.db) with a table named Product and the data contained
in the Product.csv file.

Extract the names of the Product table columns from the first line of the Product.csv file:

    "Id",
    "ProductName",
    "SupplierId",
    "CategoryId",
    "QuantityPerUnit",
    "UnitPrice",
    "UnitsInStock",
    "UnitsOnOrder",
    "ReorderLevel",
    "Discontinued",

Product table constraints are included in the product_constraints list:

    product_constraints = [
        'INTEGER PRIMARY KEY',
        'TEXT NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'TEXT NOT NULL',
        'REAL NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
    ]

Use the generate_sql() function from the previous exercise to generate the SQL that creates the Product table:

    def generate_sql(table_name, col_names, constraints):
        cols = [
            " ".join((col, constraint)).strip()
            for col, constraint in zip(col_names, constraints)
        ]
        return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'

Then create the Product table and insert data from Product.csv. In response, create a query to store.db that extracts
the number of records in the Product table and print it to the console.

In the solution, use the built-in sqlite3 package. The built-in csv module may be helpful to work with the csv file.

Expected result:

    77
"""
# Solution I
import csv
import sqlite3


def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'


with open('../Data/Product.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    col_names = next(reader)
    product_constraints = [
        'INTEGER PRIMARY KEY',
        'TEXT NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'TEXT NOT NULL',
        'REAL NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
    ]
    sql = generate_sql('Product', col_names, product_constraints)

    conn = sqlite3.connect('../Data/store.db')
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS Product''')
    conn.commit()

    cur.execute(sql)

    for row in reader:
        cur.execute(
            '''INSERT INTO Product VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row
        )

    conn.commit()

    cur.execute('''SELECT COUNT(*) FROM Product''')
    print(cur.fetchone()[0])

    conn.close()


# Solution II
product_constraints = [
    'INTEGER PRIMARY KEY',
    'TEXT NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'TEXT NOT NULL',
    'REAL NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
]


def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'


# Read csv file
with open('Product.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = tuple(reader)

# Create SQL code
sql_create_table = generate_sql(
    'Product', columns, product_constraints
)

# Create a DB connection
conn = sqlite3.connect('store.db')
cur = conn.cursor()

# Create Product table
cur.execute(sql_create_table)
cur.executemany(
    '''INSERT INTO Product VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    rows,
)
conn.commit()

# Select number of rows
cur.execute('''SELECT COUNT(*) FROM Product''')
total_rows = cur.fetchall()[0][0]
print(total_rows)

conn.close()
