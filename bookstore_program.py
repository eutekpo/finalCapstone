import sqlite3

def add_book(id, title, author, qty):
 conn = sqlite3.connect('ebookstore.db')
 cursor = conn.cursor()
 cursor.execute('''
  INSERT INTO books (id, Title, Author, Qty)
  VALUES (?,?,?,?);
  ''', (id, title, author, qty))
 conn.commit()
 print("Book added successfully.")
 conn.close()

def update_book(id, qty):
 conn = sqlite3.connect('ebookstore.db')
 cursor = conn.cursor()
 cursor.execute('''
  UPDATE books
  SET Qty = ?
  WHERE id = ?;
  ''', (qty, id))
 conn.commit()
 print("Book updated successfully.")
 conn.close()

def delete_book(id):
 conn = sqlite3.connect('ebookstore.db')
 cursor = conn.cursor()
 cursor.execute('''
  DELETE FROM books
  WHERE id = ?;
  ''', (id,))
 conn.commit()
 print("Book deleted successfully.")
 conn.close()

def search_book(title):
 conn = sqlite3.connect('ebookstore.db')
 cursor = conn.cursor()
 cursor.execute('''
  SELECT * FROM books
  WHERE Title = ?;
  ''', (title,))
 book = cursor.fetchone()
 if book:
  print("Book found:")
  print("ID:", book[0])
  print("Title:", book[1])
  print("Author:", book[2])
  print("Quantity:", book[3])
 else:
  print("Book not found.")
 conn.close()

while True:
 print("1. Enter book")
 print("2. Update a book")
 print("3. Delete a book")
 print("4. Search books")
 print("0. Exit")
 option = int(input("Enter your option: "))
 if option == 1:
  id = int(input("Enter the ID of the book: "))
  title = input("Enter the title of the book: ")
  author = input("Enter the author of the book: ")
  qty = int(input("Enter the quantity of the book: "))
  add_book(id, title, author, qty)
 elif option == 2:
  id = int(input("Enter the ID of the book you want to update: "))
  qty = int(input("Enter the new quantity: "))
  update_book(id, qty)
 elif option == 3:
  id = int(input("Enter the ID of the book you want to delete: "))
  delete_book(id)
 elif option == 4:
  title = input("Enter the title of the book you want to search for: ")
  search_book(title)
 elif option == 0:
  break
 else:
  print("Invalid option.")