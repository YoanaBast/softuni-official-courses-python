target_book = input()
command = input()
books_checked = 0

while command != 'No More Books':
    book = command

    if book == target_book:
        break

    books_checked += 1

    command = input()


if command == 'No More Books':
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
elif command == target_book:
    print(f"You checked {books_checked} books and found it.")

