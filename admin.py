from book import *
from user import *
from utility import *
from datetime import datetime


class Admin:
    def __init__(self):
        self.books = []
        self.users = {}   # key = username, value = list of books
        self.transactions = []

    # -------- BOOK --------
    def add_book(self, book_id, book_name, book_quantity):
        for book in self.books:
            if book.id == book_id:
                print("Book already exists")
                return

        self.books.append(Book(book_id, book_name, book_quantity))
        print("Book added successfully")

    def print_all_books(self):
        if not self.books:
            print("No books available")
            return

        for book in self.books:
            print(f"{book.name} (Qty: {book.quantity})")

    def search_for_book(self, query):
        return [book.name for book in self.books if query.lower() in book.name.lower()]

    # -------- USER --------
    def add_user(self, user_id, user_name):
        if user_name in self.users:
            print("User already exists!")
            return

        self.users[user_name] = []
        print("User created successfully!")

    # -------- BORROW --------
    def borrow_book(self, user_name, book_name):
        found_books = self.search_for_book(book_name)

        if not found_books:
            print("Book not found")
            return

        book_name = found_books[0]

        for book in self.books:
            if book.name == book_name:
                if book.quantity <= 0:
                    print("Book not available")
                    return
                book.quantity -= 1

        if user_name not in self.users:
            print("User not found")
            return

        self.users[user_name].append(book_name)

        self.transactions.append({
            "user": user_name,
            "book": book_name,
            "action": "borrow",
            "date": datetime.now()
        })

        print(f"{user_name} borrowed {book_name}")

    # -------- RETURN --------
    def return_book(self, user_name, book_name):
        if user_name not in self.users:
            print("User not found")
            return

        if book_name not in self.users[user_name]:
            print("User didn't borrow this book")
            return

        for book in self.books:
            if book.name == book_name:
                book.quantity += 1

        self.users[user_name].remove(book_name)

        self.transactions.append({
            "user": user_name,
            "book": book_name,
            "action": "return",
            "date": datetime.now()
        })

        print(f"{user_name} returned {book_name}")

    # -------- USERS --------
    def print_users_borrowed(self):
        for user, books in self.users.items():
            if books:
                print(f"{user} borrowed: {', '.join(books)}")
                found = True

        if not found:
            print("No users have borrowed books yet")

    def print_all_users(self):
        for user in self.users:
            print(user)

    # -------- EXTRA --------
    def print_transactions(self):
        for t in self.transactions:
            print(f"{t['user']} {t['action']} {t['book']} on {t['date']}")

    def most_borrowed_book(self):
        count = {}

        for t in self.transactions:
            if t["action"] == "borrow":
                count[t["book"]] = count.get(t["book"], 0) + 1

        if not count:
            print("No data")
            return

        max_book = max(count, key=count.get)
        print(f"Most borrowed: {max_book} ({count[max_book]} times)")
