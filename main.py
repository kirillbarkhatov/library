from src.book import Book
from src.library import Library




if __name__ == "__main__":
    book_1 = Book("Книга 1", "Автор 1", 2000)
    book_2 = Book("Книжище", "Автор 2", 2000)
    book_3 = Book("Книга 3", "Петя", 2000)

    library = Library()
    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)

    print(library)
    library.print_all_book()
    library.search_book("книааа")