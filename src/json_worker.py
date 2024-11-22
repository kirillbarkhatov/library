import json
from typing import Any

class JSONWorker:
    """Класс для работы с json файлами"""

    __file_name: str  # имя файла
    path_to_file: str = "data/"  # путь до файла
    path_with_filename: str  # путь до файла вместе с именем файла

    def __init__(self, file_name: str = "library.json") -> None:
        self.__file_name = self.__check_and_get_file_name(file_name)

    def save_to_file(self, library: list[dict]) -> None:
        """Метод для сохранения в файл"""

        with open(self.path_to_file + self.__file_name, "w", encoding="UTF-8") as file:
            json.dump(library, file, indent=4, ensure_ascii=False)

    def get_from_file(self) -> Any:
        """Метод для получения данных из файла"""

        with open(self.path_to_file + self.__file_name, "r", encoding="UTF-8") as file:
            return json.load(file)

    def delete_from_file(self) -> None:
        """Метод для удаления данных из файла"""

        self.save_to_file([])

    @staticmethod
    def __check_and_get_file_name(file_name: str) -> str:
        if file_name[-5:] != ".json":
            return f"{file_name}.json"
        return file_name
