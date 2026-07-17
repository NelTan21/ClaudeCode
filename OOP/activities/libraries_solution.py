class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        new_books: list[Book] = []
        for lib_book in self.books:
            if lib_book.title != book.title or lib_book.author != book.author:
                new_books.append(lib_book)
        self.books = new_books

    def search_books(self, search_string: str) -> list[Book]:
        results: list[Book] = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower()
                or search_string.lower() in book.author.lower()
            ):
                results.append(book)
        return results
