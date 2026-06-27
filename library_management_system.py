from datetime import datetime, timedelta

# Create Library Dictionary
library = {}

# Question 1: Add Book
def add_book():
    isbn = input("Enter ISBN Number: ")

    if isbn in library:
        print("Book already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None,
        "issue_date": None
    }

    print("Book added successfully!")


# Question 2: Issue Book
def issue_book():
    isbn = input("Enter ISBN Number: ")

    if isbn not in library:
        print("Book not found!")
        return

    if library[isbn]["available"]:
        borrower = input("Enter Borrower Name: ")

        library[isbn]["available"] = False
        library[isbn]["borrower"] = borrower

        issue_date = datetime.now()
        library[isbn]["issue_date"] = issue_date

        due_date = issue_date + timedelta(days=7)

        print("Book issued successfully!")
        print("Due Date:", due_date.strftime("%d-%m-%Y"))

    else:
        print("Book already issued!")


# Question 3: Return Book
def return_book():
    isbn = input("Enter ISBN Number: ")

    if isbn not in library:
        print("Book not found!")
        return

    if not library[isbn]["available"]:
        library[isbn]["available"] = True
        library[isbn]["borrower"] = None
        library[isbn]["issue_date"] = None

        print("Book returned successfully!")

    else:
        print("Book is already available.")


# Question 4: Search Book
def search_book():
    keyword = input("Enter Title or Author: ").lower()

    for isbn, details in library.items():
        if keyword in details["title"].lower() or keyword in details["author"].lower():
            print("ISBN :", isbn)
            print("Title :", details["title"])
            print("Author :", details["author"])
            print("Status :", "Available" if details["available"] else "Issued")


# Question 5: View Catalog
def view_catalog():
    if len(library) == 0:
        print("Library is empty.")
    else:
        for isbn, details in library.items():
            print("ISBN :", isbn)
            print("Title :", details["title"])
            print("Author :", details["author"])
            print("Status :", "Available" if details["available"] else "Issued")


# Main Program
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Catalog")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        issue_book()

    elif choice == 3:
        return_book()

    elif choice == 4:
        search_book()

    elif choice == 5:
        view_catalog()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")