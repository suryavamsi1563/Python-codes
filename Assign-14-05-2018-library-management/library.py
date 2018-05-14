class Library:
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books

    def add_book(self, book, category):
        self.list_of_books.append(book)
        print("Book added to the " + category)
        print("Present books in " + category + "\n")
        print(show_books(enumerate(self.list_of_books, 1)))

    def remove_book(self, book, category):
        if book in self.list_of_books:
            self.list_of_books.remove(book)
            print("Book is removed from the " + category)
            print("Present books in " + category + "\n")
            print(show_books(enumerate(self.list_of_books, 1)))
        else:
            print("Book not  present in the " + category)


class Customer(Library):
    def __init__(self, taken_books):
        self.taken_books = taken_books

    def return_book(self, book, category):
        if book in self.taken_books:
            category.add_book(book, display[Category])
            self.taken_books.remove(book)
        else:
            print("Book never taken")

    def borrow_book(self, book, category):
        if book in self.taken_books:
            print("Book already Taken by you.")
        else:
            if book not in choice[Category].list_of_books:
                return "Please enter the book from the list."
            category.remove_book(book, display[Category])
            self.taken_books.append(book)
            print("Books Taken by you are : ")
            show_books(enumerate(self.taken_books, 1))


Fiction = Library(['Sherlock Holmes', 'Gulliver Travels', 'Adventures of Tom Sawyer', 'Fire & Ashes'])
Mythology = Library(['Ramayana', 'Mahabharath','Greek', 'Norse'])
Stories = Library(['Panchathanthram', 'Arabian knights', 'Sinbad'])

choice = {1: Fiction, 2: Mythology, 3: Stories}

display = {1: "Fiction", 2: "Mythology", 3: "Stories"}
Customer1 = Customer([])

def show_books(x):
    for count, book in x:
        print(count, book)
    return ''

while True:
    Category = int(input(
        "Enter the options for the below Category\n "
        "1. Fiction \n "
        "2. Mythology \n "
        "3. Stories.\n "
        "Please enter the number: "))

    print("Selected category is :" + display[Category])

    Action = int(input("Select the action to be performed from the following.\n"
                       "1. Add a book to the " + display[Category] + "\n"
                                                                     "2. Return a book \n"
                                                                     "3. Borrow the book \n"
                                                                     "4. Show the taken books \n"
                                                                     "Enter the choice as number : "))

    if Action == 1:
        book_name = input("Enter the book name to be added.")
        choice[Category].add_book(book_name, display[Category])

    elif Action == 2:
        show_books(enumerate(Customer1.taken_books, 1))
        book_name = input("Enter the book name to be returned from the above list :")
        Customer1.return_book(book_name, choice[Category])

    elif Action == 3:
        show_books(enumerate(choice[Category].list_of_books, 1))
        book_name = input("Enter the book name you want to borrow from the above list :")
        Customer1.borrow_book(book_name, choice[Category])

    elif Action == 4:
        print("Taken Books are as follows.")
        show_books(enumerate(Customer1.taken_books, 1))

    run = input("Do you wish to perform another action.\n"
                "Enter 'yes' if you want to : ").upper()

    if run == 'YES':
        continue
    else:
        break
