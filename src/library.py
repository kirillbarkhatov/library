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

    def delete_book(self, id: int) -> None:
        """Функция для удаления книги"""

        ids = self.__get_list_ids()
        try:
            index_for_delete = ids.index(id)
            del self.books[index_for_delete]
        except ValueError:
            print(f"Книги с id={id} нет в библиотеке")

    def search_book(self):
        """Функция для поиска книги"""

        pass

    def print_all_book(self):
        """Функция для вывода всех книг"""

        for book in self.books:
            print(book)

    def __get_list_ids(self) -> list[int]:
        """Функция для получения списка всех id книг в библиотеке"""

        return [book.id for book in self.books]

    def __get_last_book_id(self) -> int:
        """Функция для получения наибольшего id книги, имеющейся в библиотеке"""

        ids = self.__get_list_ids()
        if not ids:
            return 0
        max_id = max(ids)
        return max_id

