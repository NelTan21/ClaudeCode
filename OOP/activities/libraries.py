class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        print(f"Created Book:{self.title} Authored by:{self.author}")


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = []
        print(f"Created a new Library:{self.name} there should be no booklist{self.books}")        

    def add_book(self, book: Book) -> None:
        new_book = (book.title, book.author)
        print(f"Adding New Book:{new_book}")
        self.books.append(new_book)
        print(f"Current Library list for {self.name} after adding new book:{self.books}")

    def remove_book(self, book: Book) -> None:
        print(f"This is the book that needs to be removed{(book.title, book.author)}")
        held_books = []
        print(f"Creating a new list for held books:{held_books}")
        for books in self.books:
            print(f"Checking if book:({books}) should be kept...")
            print(f"List of books to be checked:({self.books})")
            if books != (book.title, book.author):
                held_books.append(books)
                print(f"Adding held books during the removal process:{held_books}")
        self.books = held_books
        print(f"This is the updated booklist after the removal process:{self.books}")
            

    def search_books(self, search_string: str) -> list[Book]:
        search_string = search_string.lower()
        print(f"This is the result of the lower cased search string:{search_string}")
        searched_books = []
        
        print(f"This is a the result prior to searching for a book:{searched_books}")
        for title,author in self.books:
            print(f"This is the iteration for Title/Author Pairs({title,author}) in the booklist:{self.books}")
            for word in title,author:
                print(f"This is the iteration for word({word}) in the Title/Author key pairs:({title,author})") 
                if search_string in word.lower():
                    print(f"This is the string being searched({search_string}) which is being matched to current word({word})")
                    searched_books.append((Book(title,author)))
                    continue
                print(f"Added {title,author} to searched books")
            print(f"Searched books current list:{searched_books}")    
        return searched_books
