import sqlite3

# Create a new database or connect to an existing one
with sqlite3.connect('product_database.db') as conn:
    cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id_product INTEGER PRIMARY KEY,
    color TEXT NOT NULL,
    type TEXT NOT NULL
)
''')

# Insert sample data into the table
cursor.execute('''
INSERT INTO products (id_product, color, type) VALUES
(001, 'red', 'face'),
(002, 'yellow', 'face'),
(003, 'red', 'lip')
''')



# Create the effects table
cursor.execute('''
CREATE TABLE IF NOT EXISTS effects (
    degree INTEGER NOT NULL,
    affect TEXT NOT NULL
)
''')

# Insert sample data into the effects table
cursor.execute('''
INSERT INTO effects (degree, affect) VALUES (?, ?)
''', [
    (1, 'light'),
    (2, 'dark')
])



# Commit and close the connection
conn.commit()
conn.close()