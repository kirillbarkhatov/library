from typing import Any


from src.json_worker import JSONWorker
from src.utils import file_data_info
from src.book import Book
from src.library import Library



class UI:

    # # Цвета
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    @staticmethod
    def lets_go() -> None:
        """Функция запускающая программу"""

        print(f"{UI.GREEN}=====================================================")
        print("Консольное приложение для управления библиотекой книг")
        print(f"====================================================={UI.RESET}")
        print("Выберите действие:")
        print("1. Инициализировать/создать новую пустую библиотеку")
        print('2. Получить инф-ю об имеющихся библиотеках (хранятся в "data/", поддерживаемые форматы: json)')
        choice = 0

        while choice not in [1, 2]:
            try:
                choice = int(input("Введите 1 или 2: "))
                if choice not in [1, 2]:
                    print("Повторите ввод")
            except ValueError:
                print("Повторите ввод")

        print()
        match choice:
            case 1:
                UI.working_with_new_library()
            case 2:
                UI.working_with_exist_library()

    @staticmethod
    def working_with_new_library() -> Any:
        """Функция для взаимодействия с пользователем при работе с новой пустой библиотекой"""

        library = Library()
        print(f"{UI.YELLOW}Создана пустая библиотека с именем {library.name}{UI.RESET}")
        print()
        return UI.library_working(library)

    @staticmethod
    def working_with_exist_library() -> None:
        """Получение данных из существующей библиотеки"""

        files = file_data_info()
        if len(files) == 0:
            print(f"{UI.YELLOW}Доступные для работы файлы отсутствуют{UI.RESET}")
            UI.working_with_new_library()
        else:
            print(f"{UI.GREEN}Для дальнейшей работы доступны следующие файлы: {UI.RESET}")
            for i in range(len(files)):
                print(f"{i + 1}. {files[i]}")
            file_for_work = input("Введите имя требуемого файла: ")
            file_worker = JSONWorker(file_for_work)
            books = file_worker.get_from_file()
            library = Library(file_for_work)
            library.add_books_from_list(books)
            print(f"{UI.YELLOW}Данные загружены из файла{UI.RESET}")
            UI.library_working(library)

    # @staticmethod
    # def file_working(file_name: str) -> Any:
    #     """Функция интерфейса для выбора опций загрузки данных о вакансиях из файла"""
    #
    #     if file_name[-5:] == ".json":
    #         file_worker = JSONWorker(file_name)
    #     elif file_name[-5:] == ".xlsx":
    #         file_worker = ExcelWorker(file_name)
    #     else:
    #         print("Неверно введено имя файла")
    #         return UI.files_info_and_choice()
    #
    #     print("Доступные действия: ")
    #     print("1. Загрузить все вакансии из файла")
    #     print("2. Очистить файл")
    #     choice = int(input("Выберите 1 или 2: "))
    #     if choice == 1:
    #         vacancies_list = file_worker.get_from_file()
    #         vacancies_objects = Vacancy.get_list_of_vacancies(vacancies_list)
    #         print(f"Количество загруженных вакансий - {len(vacancies_objects)}")
    #         return UI.vacancies_working(vacancies_objects)
    #
    #     elif choice == 2:
    #         file_worker.delete_from_file()
    #         print("Файл очищен")
    #         return UI.files_info_and_choice()
    #
    #     else:
    #         return UI.file_working(file_name)

    @staticmethod
    def library_working(library: Library) -> None:
        """Работа с библиотекой - доступ к функционалу"""

        print(f'{UI.GREEN}Библиотека "{library.name}". {library}{UI.RESET}')
        print("Доступны следующие действия для работы с библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Посмотреть список книг")
        print("4. Найти книгу")
        print("5. Выдать/принять книгу (сменить статус книги)")
        print("6. Добавить книги из другой библиотеки (файла json)")
        print("7. Сохранить изменения в библиотеке (в файл json)")
        print("8. Переименовать библиотеку")
        print("9. Завершить работу и выйти (данные будут автоматически сохранены)")
        choice = 0
        while choice not in range(1, 10):
            try:
                choice = int(input("Введите цифру от 1 до 9 для выбора действия: "))

                if choice not in range(1, 10):
                    print("Повторите ввод")
            except ValueError:
                print("Повторите ввод")

        match choice:

            case 1:
                # 1. Добавить книгу
                UI.choice_1_add_book(library)

            case 2:
                # 2. Удалить книгу
                UI.choice_2_delete_book(library)

            case 3:
                # 3. Посмотреть список книг
                UI.choice_3_books_list(library)

            case 4:
                # 4. Найти книгу
                UI.choice_4_search_books(library)

            case 5:
                # 5. Выдать/принять книгу (сменить статус книги)
                UI.choice_5_search_books(library)

            case 6:
                # 6. Добавить книги из другой библиотеки (файла json)
                UI.choice_6_add_from_library(library)

            case 7:
                # 7. Сохранить изменения в библиотеке (в файл json)
                pass

            case 8:
                # 8. Переименовать библиотеку
                pass

            case 9:
                # 9. Завершить работу и выйти (данные будут автоматически сохранены)
                pass

    @staticmethod
    def choice_1_add_book(library: Library) -> None:
        """Интерфейс добавления книги"""

        print()
        print("Добавляем новую книгу в библиотеку")
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")

        year = 0
        while year // 1000 not in (1, 2):
            try:
                year = int(input("Введите год издания книги в формате YYYY: "))

                if year // 1000 not in (1, 2):
                    print("Повторите ввод")
            except ValueError:
                print("Повторите ввод")

        library.add_book(Book(title, author, year))
        print(f"{UI.YELLOW}Книга добавлена в библиотеку{UI.RESET}")
        print()
        UI.library_working(library)

    @staticmethod
    def choice_2_delete_book(library: Library) -> None:
        """Интерфейс удаления книги"""

        print()
        print("Библиотека содержит следующие книги:")
        library.print_all_book()
        print()

        book_id = 0

        while book_id < 1:
            try:
                book_id = int(input(f"{UI.RED}Введите индекс книги для её удаления: {UI.RESET}"))

                if book_id < 1:
                    print("Повторите ввод")
            except ValueError:
                print("Повторите ввод")

        library.delete_book(book_id)
        print(f"{UI.YELLOW}Книга удалена{UI.RESET}")
        print()
        UI.library_working(library)

    @staticmethod
    def choice_3_books_list(library: Library) -> None:
        """Интерфейс вывода списка книг"""

        print()
        print("Библиотека содержит следующие книги:")
        library.print_all_book()
        print()
        UI.library_working(library)

    @staticmethod
    def choice_4_search_books(library: Library) -> None:
        """Интерфейс вывода списка книг"""

        print()
        search_request = input("Введите название, автора или год выпуска книги для поиска: ")
        library.search_book(search_request)
        print()
        UI.library_working(library)

    @staticmethod
    def choice_5_search_books(library: Library) -> None:
        """Интерфейс смены статуса книги"""

        print()
        print("Библиотека содержит следующие книги:")
        library.print_all_book()
        print()
        book_id = int(input("Введите введите индекс книги для смены статуса: "))
        book_status = input('Введите новый статус: "в наличии" или "выдана": ')
        library.change_book_status(book_id, book_status)
        print()
        UI.library_working(library)

    @staticmethod
    def choice_6_add_from_library(library: Library) -> None:
        """Получение данных из существующей библиотеки"""

        files = file_data_info()
        if len(files) == 0:
            print(f"{UI.YELLOW}Доступные для работы файлы отсутствуют{UI.RESET}")
            UI.library_working(library)
        else:
            print(f"{UI.GREEN}Для дальнейшей работы доступны следующие файлы: {UI.RESET}")
            for i in range(len(files)):
                print(f"{i + 1}. {files[i]}")
            file_for_work = input("Введите имя требуемого файла: ")
            file_worker = JSONWorker(file_for_work)
            books = file_worker.get_from_file()
            library.add_books_from_list(books)
            print(f"{UI.YELLOW}Данные загружены из файла{UI.RESET}")
            UI.library_working(library)

    # @staticmethod
    # def save_to_file(vacancies: list) -> None:
    #     """Функция интерфейса для выбора опций сохранения данных в файл"""
    #
    #     print("Выберете формат файла в которых нужно сохранить полученные вакансии: ")
    #     print("1. json")
    #     print("2. excel")
    #
    #     file_format = 0
    #     while file_format not in [1, 2]:
    #         try:
    #             file_format = int(input("Введите цифру 1 или 2 для выбора формата файла: "))
    #             if file_format not in [1, 2]:
    #                 print("Повторите ввод")
    #         except ValueError:
    #             print("Повторите ввод")
    #
    #     file_name = input("Введите желаемое имя файла или пропустите ввод (имя по умолчанию - vacancies): ")
    #     vacancies_to_save = Vacancy.get_list_of_dicts_vacancies(vacancies)
    #     match file_format:
    #         case 1:
    #             if len(file_name) > 0:
    #                 json_saver = JSONWorker(file_name)
    #             else:
    #                 json_saver = JSONWorker()
    #                 file_name = "vacancies"
    #             try:
    #                 json_saver.add_to_file(vacancies_to_save)
    #                 print(f"Данные успешно добавлены в файл {file_name}.json")
    #             except (FileNotFoundError, KeyError, TypeError):
    #                 json_saver.save_to_file(vacancies_to_save)
    #                 print(f"Данные успешно сохранены в файл {file_name}.json")
    #
    #         case 2:
    #             if len(file_name) > 0:
    #                 excel_saver = ExcelWorker(file_name)
    #             else:
    #                 excel_saver = ExcelWorker()
    #                 file_name = "vacancies"
    #             try:
    #                 excel_saver.add_to_file(vacancies_to_save)
    #                 print(f"Данные успешно добавлены в файл {file_name}.xlsx")
    #             except (FileNotFoundError, KeyError, TypeError):
    #                 excel_saver.save_to_file(vacancies_to_save)
    #                 print(f"Данные успешно сохранены в файл {file_name}.xlsx")
