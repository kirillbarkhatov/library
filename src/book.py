

class Book:
    """Класс для работы с книгами"""

    __id: int | None
    title: str
    author: str
    year: int
    __status: str

    def __init__(self, title: str, author: str, year: int) -> None:
        """Создание экземпляра книги"""

        self.__id = None
        self.title = title
        self.author = author
        self.year = year
        self.__status = "в наличии"


    def __str__(self):
        """Вывод данных о книге"""
        return f"{(str(self.id) + " " * 5)[:5]} | {(self.title + " " * 30)[:30]} | {(self.author + " " * 15)[:15]} | {self.year} | {self.status}"

    @property
    def id(self) -> int:
        """Функция для получения id книги"""

        return self.__id

    @id.setter
    def id(self, uniq_id: int) -> None:
        """Функция для присвоения уникального id книги"""

        self.__id = uniq_id

    @property
    def status(self) -> str:
        """Функция для получения статуса книги"""

        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        """Функция для присвоения статуса книги"""

        if status.lower() in ("в наличии", "выдана"):
            self.__status = status.lower()
        else:
            print('Введите корректный статус: "в наличии" или "выдана"')

    @classmethod
    def from_dict(cls, book_dict):
        """Получить объект из словаря"""

        title = book_dict["title"]
        author = book_dict["author"]
        year = book_dict["year"]
        status = book_dict["_Book__status"]
        book = cls(title, author, year)
        book.status = status
        return book

