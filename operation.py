import data
import datetime


def add_book():
    name = input("Enter book name: ").lower()
    if name in data.books:
        print("Book already exists.")
    else:
        data.books[name] = {"available": True}
        print(f"'{name}' added successfully.")


def view_book():
    print("\n Available Books:")
    found = False
    for book, info in data.books.items():
        if info["available"]:
            print("•", book)
            found = True
    if not found:
        print("No books available.")



def issued_book():
    if not data.books:
        print("No books available.")
        return

    name = input("\nEnter book name to issue: ").lower()

    if name in data.books and data.books[name]["available"]:
        student = input("Enter student name: ")
        days = int(input("Enter number of days: "))

        issue_date = datetime.date.today()

        data.issued_books[name] = {
            "student": student,
            "days": days,
            "issue_date": issue_date
        }

        data.books[name]["available"] = False

        print(f"\n'{name}' issued to {student} for {days} days on {issue_date}")
        print(" Note: Late return will be fined based on weekly rate.")

    else:
        print("Book not available.")



def calculate_fine(late_days):
    fine = 0
    for i in range(1, late_days + 1):
        week = (i - 1) // 7 + 1
        rate = 10
        for j in range(1, week + 1):
            rate *= j
        fine += rate
    return fine


def return_book():
    name = input("\nEnter book name to return: ").lower()

    if name in data.issued_books:
        record = data.issued_books[name]
        issue_date = record["issue_date"]
        allowed_days = record["days"]

        today = datetime.date.today()
        total_days = (today - issue_date).days

        print(f"\nReturned by: {record['student']}")

        if total_days > allowed_days:
            late_days = total_days - allowed_days
            fine = calculate_fine(late_days)
            print(f" Late by {late_days} days. Fine = ₹{fine}")
        else:
            print(" Returned on time. No fine.")

        data.books[name]["available"] = True
        del data.issued_books[name]

        print(f"'{name}' returned successfully.")

    else:
        print("Invalid return. Book not issued.")