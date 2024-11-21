

class Book:
    """Класс для работы с книгами"""

    __id: int | None
    title: str
    author: str
    year: int
    status: str

    def __init__(self, title: str, author: str, year: int) -> None:
        """Создание экземпляра книги"""

        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"
        self.__id = None

    def __str__(self):
        return f"{self.id}. {self.title} - {self.author} // {self.year} - {self.status}"


    @property
    def id(self) -> int:
        """Функция для получения id книги"""

        return self.__id

    @id.setter
    def id(self, uniq_id: int) -> None:
        """Функция для присвоения уникального id книги"""

        self.__id = uniq_id
