import os

from src.book import Book
from src.json_worker import JSONWorker


def file_data_info() -> list:
    """Функция для получения данных о файлах в папке data"""

    path = "data/"
    files = []
    for dir_entry in os.scandir(path):
        if dir_entry.is_file():
            files.append(dir_entry.name)
    print(f"В папке {path} содержится {len(files)} файл(а)(ов):")
    checked_files = []
    for file in files:
        try:
            if file[-5:] == ".json":
                checking_file = JSONWorker(file)
            else:
                raise TypeError
            file_data = checking_file.get_from_file()
            if len(file_data) == 0:
                raise TypeError

            books_count = 0
            for book in file_data:
                try:
                    Book.from_dict(book)
                    books_count += 1
                except KeyError:
                    pass
            if books_count == 0:
                raise TypeError
            checked_files.append(file)
            print(f"{file} - содержит {books_count} книг(и)")
        except TypeError:
            print(f"{file} - файл не содержит данных о вакансиях или формат файла не поддерживается")
        except FileNotFoundError:
            print(f"{file} - файл не содержит данных о вакансиях или формат файла не поддерживается")

    return checked_files
