from admin import *
from utility import input_is_valid

class OperationsManager:
    def __init__(self):
        self.admin = Admin()

    def print_menu(self):
        print("\nProgram Options:")
        options = [
            '1) Add book',
            '2) Print library books',
            '3) Search books',
            '4) Add user',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print users',
            '9) Print transactions',
            '10) Most borrowed book',
            '0) Exit'
        ]
        print('\n'.join(options))

        return input_is_valid("Enter choice: ", 0, 10)

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.admin.add_book(
                    input("Book ID: "),
                    input("Book Name: "),
                    input("Quantity: ")
                )

            elif choice == 2:
                self.admin.print_all_books()

            elif choice == 3:
                books = self.admin.search_for_book(input("Search: "))
                print(", ".join(books) if books else "No books found")

            elif choice == 4:
                self.admin.add_user(
                    int(input("User ID: ")),
                    input("User Name: ")
                )

            elif choice == 5:
                self.admin.borrow_book(
                    input("User Name: "),
                    input("Book Name: ")
                )

            elif choice == 6:
                self.admin.return_book(
                    input("User Name: "),
                    input("Book Name: ")
                )

            elif choice == 7:
                self.admin.print_users_borrowed()

            elif choice == 8:
                self.admin.print_all_users()

            elif choice == 9:
                self.admin.print_transactions()

            elif choice == 10:
                self.admin.most_borrowed_book()

            elif choice == 0:
                print("Exiting...")
                break

            else:
                print("Invalid choice")