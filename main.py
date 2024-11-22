from src.book import Book
from src.library import Library
from src.json_worker import JSONWorker
from src.utils import file_data_info




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
    library.change_book_status(2,"вЫдана")
    library.print_all_book()
    library.change_book_status(3, "вЫдана")
    library.print_all_book()
    library.delete_book(3)
    library.print_all_book()
    books = library.get_books_list()
    json_worker = JSONWorker()
    # json_worker.save_to_file(books)

    print(file_data_info())