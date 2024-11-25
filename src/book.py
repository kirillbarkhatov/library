from typing import Any


class Book:
    """Класс для работы с книгами"""

    __id: int | None
    title: str
    author: str
    year: int
    __status: str

    def __init__(self, title: str, author: str, year: int) -> None:
        """Создание экземпляра книги"""

        Book.__input_validation(title, author, year)
        self.__id = None
        self.title = title
        self.author = author
        self.year = year
        self.__status = "в наличии"

    def __str__(self) -> str:
        """Вывод данных о книге"""
        return f"{(str(self.id) + " " * 5)[:5]} | {(self.title + " " * 30)[:30]} | {(self.author + " " * 15)[:15]} | {self.year} | {self.status}"

    @property
    def id(self) -> int | None:
        """Метод для получения id книги"""

        return self.__id

    @id.setter
    def id(self, uniq_id: int) -> None:
        """Метод для присвоения уникального id книги"""

        self.__id = uniq_id

    @property
    def status(self) -> str:
        """Метод для получения статуса книги"""

        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        """Метод для присвоения статуса книги"""

        if status.lower() in ("в наличии", "выдана"):
            self.__status = status.lower()
        else:
            print('Введите корректный статус: "в наличии" или "выдана"')

    @classmethod
    def from_dict(cls, book_dict: dict) -> Any:
        """Получить объект из словаря"""

        title = book_dict["title"]
        author = book_dict["author"]
        year = book_dict["year"]
        status = book_dict.get("_Book__status", "в наличии")
        book = cls(title, author, year)
        book.status = status
        return book

    @staticmethod
    def __input_validation(title: str, author: str, year: int) -> Any:
        """Валидация полученных атрибутов"""

        if not title or not author or not year:
            raise TypeError("В атрибутах передан None")

        if not isinstance(title, str) or not isinstance(author, str) or not isinstance(year, int):
            raise TypeError("Неправильный тип данных")

        if year // 1000 not in (1, 2):
            raise ValueError("Ожидается год в формате 1YYY или 2YYY")
