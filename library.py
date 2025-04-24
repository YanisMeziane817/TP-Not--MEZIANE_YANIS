class Person:
    """Class representing a person in the library"""
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.__repr__()
    
class Book:
    """Class representing a book in the Library"""
    def __init__(self, title: str, author: Person):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"{self.title} ({self.author})"
    
    def __str__(self):
        return self.__repr__()


class LibraryError(Exception):
    """Base class for Library errors"""
    pass


class Library:
    """Class representing a library"""
    def __init__(self, name: str):
        self.name = name
        self._books = []
        self._members = set()
        self._borrowed_books = {}
    
    def is_book_available(self, book: Book) -> bool:
        """Check if a book is available for borrowing"""
        if book not in self._books:
            raise LibraryError(f"{book} doesn't exist in the library")
        return book not in self._borrowed_books
    
    def borrow_book(self, book: Book, person: Person):
        """Borrow a book from the library"""
        if person not in self._members:
            raise LibraryError(f"{person} is not a member of the library")
        if book not in self._books:
            raise LibraryError(f"{book} doesn't exist in the library")
        if not self.is_book_available(book):
            raise LibraryError(f"{book} is already borrowed by {self._borrowed_books[book]}")
        
        self._borrowed_books[book] = person
    
    def return_book(self, book: Book):
        """Return a book to the library"""
        if book not in self._borrowed_books:
            raise LibraryError(f"{book} is not part of the borrowed books")
        
        del self._borrowed_books[book]
    
    def add_new_member(self, person: Person):
        """Add a new member to the library"""
        self._members.add(person)
    
    def add_new_book(self, book: Book):
        """Add a new book to the library's catalog"""
        self._books.append(book)
    
    def print_status(self):
        """Print the current status of the library"""
        available_books = [book for book in self._books if book not in self._borrowed_books]
        
        print(f"{self.name} status:")
        print(f"Books catalogue: {self._books}")
        print(f"Members: {self._members}")
        print(f"Available books: {available_books}")
        print(f"Borrowed books: {self._borrowed_books}")
        print("-----")


def main():
    """Test your code here"""
    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()

    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()

    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()



if __name__ == "__main__":
     main()