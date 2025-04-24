class Person:
    """class representing a person in the library"""
    def __init__(self, first_name :str, last_name :str):
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.__repr__()

antoine = Person("Antoine", "Dupont")
print(antoine)


class Book:
    """class representing a book in the Library"""
    def __init__(self, title :str , author :str ):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"{self.title} by {self.author}"
    def __str__(self):
        return self.__repr__()
    
novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
print(novel_book)


class LibraryError(Exception):
    """Base class for Library errors"""
    


class Library:
    """class representing a library"""
    def __init__(self, name :str , _books :str, _members :str , _borrowed_books :str):
        self.name = name
        self._books = _books
        self._members = _members
        self._borrowed_books = _borrowed_books
    
    def is_available(book :Book) -> bool:
        pass


    def borrow_book(book: Book , person: Person) :
        pass

    def return_book(book: Book ):
        pass

    def add_new_member(person: Person):
        pass
    def add_new_book(book: Book):
        pass

    def print_status(self) :
        pass


def main():
    """Test your code here"""
    

if __name__ == "__main__":
    main()
