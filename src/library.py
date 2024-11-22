from src.book import Book

class Library:
    """Класс для работы с библиотекой"""

    name: str
    books: list


    def __init__(self, name: str = "library") -> None:
        """Инициализация библиотеки"""

        self.name = name
        self.books = []

    def __str__(self):
        """Вывод информации о библиотеке"""

        return f"В библиотеке содержится {len(self.books)} книг(и)"

    def add_book(self, book: Book) -> None:
        """Функция для добавления книги"""

        book.id = self.__get_last_book_id() + 1
        self.books.append(book)

    def __get_book_index_via_id(self, book_id: int) -> int:
        """Получение экземпляра книги по id"""

        ids = self.__get_list_ids()
        book_index = ids.index(book_id)
        return book_index

    def change_book_status(self, book_id, status) -> None:
        """Изменение статуса книги"""

        try:
            book_index = self.__get_book_index_via_id(book_id)
            self.books[book_index].status = status
        except ValueError:
            print(f"Книги с id={book_id} нет в библиотеке")

    def delete_book(self, book_id: int) -> None:
        """Функция для удаления книги"""

        try:
            index_for_delete = self.__get_book_index_via_id(book_id)
            del self.books[index_for_delete]
        except ValueError:
            print(f"Книги с id={book_id} нет в библиотеке")

    def search_book(self, search_request: str) -> None:
        """Функция для поиска книг"""

        result = [
            book
            for book in self.books
            if Library.__search_in_title(book, search_request)
            or Library.__search_in_author(book, search_request)
            or Library.__search_in_year(book, search_request)
        ]

        if not result:
            print("Книг по вашему запросу не найдено")

        header = f"{("#" + " " * 5)[:5]} | {("Название" + " " * 30)[:30]} | {("Автор" + " " * 15)[:15]} | Год  | Статус"
        header_index = 0
        for book in result:
            if header_index % 5 == 0:
                print()
                print(header)
                print()
            print(book)
            header_index += 1

    @staticmethod
    def __search_in_title(book: Book, search_request: str) -> bool:
        """Функция для поиска в названии"""

        return search_request.lower() in book.title.lower()

    @staticmethod
    def __search_in_author(book: Book, search_request: str) -> bool:
        """Функция для поиска по автору"""

        return search_request.lower() in book.author.lower()

    @staticmethod
    def __search_in_year(book: Book, search_request: str) -> bool:
        """Функция для поиска по автору"""

        return search_request.lower() == str(book.year).lower()

    def print_all_book(self):
        """Функция для вывода всех книг"""

        header = f"{("#" + " " * 5)[:5]} | {("Название" + " " * 30)[:30]} | {("Автор" + " " * 15)[:15]} | Год  | Статус"
        header_index = 0
        for book in self.books:
            if header_index % 5 == 0:
                print()
                print(header)
                print()
            print(book)
            header_index += 1

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

    def get_books_list(self) -> list[dict]:
        """Получить список книг"""

        return [book.__dict__ for book in self.books]

    def add_books_from_list(self, books: list) -> None:
        """Добавить книги из списка книг"""

        try:
            for book in books:
                self.add_book(Book.from_dict(book))
        except KeyError:
            pass

