from src.book import Book

class Library:
    """Класс для работы с библиотекой"""

    books: list

    def __init__(self) -> None:
        """Инициализация библиотеки"""

        self.books = []

    def __str__(self):
        """Вывод информации о библиотеке"""

        return f"В библиотеке содержится {len(self.books)} книг(и)"

    def add_book(self, book: Book) -> None:
        """Функция для добавления книги"""

        book.id = self.__get_last_book_id() + 1
        self.books.append(book)

    def delete_book(self):
        """Функция для удаления книги"""

        pass

    def search_book(self):
        """Функция для поиска книги"""

        pass

    def print_all_book(self):
        """Функция для вывода всех книг"""

        for book in self.books:
            print(book)

    def __get_last_book_id(self) -> int:
        """Функция для получения наибольшего id книги, имеющейся в библиотеке"""

        ids = [book.id for book in self.books]
        if not ids:
            return 0
        max_id = max(ids)
        return max_id

