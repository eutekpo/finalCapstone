# Ebook Store Database

## Description

This project is a simple database program for an ebook store. The database is built using SQLite and Python. It includes a table called "books" that stores information about books, such as the book's ID, title, author, and quantity.

## Table of Contents

- Installation
- Usage
- Credits

## Installation

To install the ebook store database program, you will need to have Python and SQLite installed on your machine. You can download Python from the official website [here](https://www.python.org/downloads/). SQLite is included with Python, so there is no need to install it separately.

Once you have Python and SQLite installed, clone the repository to your local machine. You can do this by running the following command in your terminal or command prompt:

```git clone https://github.com/<username>/ebookstore.git```

Replace `<username>` with your GitHub username.

Next, navigate to the ebookstore directory and run the `ebookstore.py` file using Python.

```cd ebookstore
python ebookstore.py```

This will create the ebookstore database and populate the "books" table with the specified data.

## Usage

To use the ebook store database program, you can run SQL commands using the SQLite command-line interface. You can start the SQLite command-line interface by running the following command:

```sqlite3 ebookstore.db```

Once you are in the SQLite command-line interface, you can run SQL commands to interact with the ebookstore database. For example, you can run the following command to display the contents of the "books" table:

```SELECT * FROM books;```

You can also run the example Python code provided in this repository to perform various operations on the "books" table, such as inserting data into the table, updating data in the table, or deleting data from the table.
