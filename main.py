import operation

while True:
    print("""

1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Exit

""")

    choice = input("Enter your choice: ")

    if choice == "1":
        operation.add_book()

    elif choice == "2":
        operation.view_book()

    elif choice == "3":
        operation.issued_book()

    elif choice == "4":
        operation.return_book()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")