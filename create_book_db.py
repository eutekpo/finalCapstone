import sqlite3

conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE books (
  id INTEGER,
  Title TEXT,
  Author TEXT,
  Qty INTEGER
);
''')
               
data = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

cursor.executemany('''
INSERT INTO books (id, Title, Author, Qty)
VALUES (?,?,?,?);
''', data)               

conn.commit()
conn.close()