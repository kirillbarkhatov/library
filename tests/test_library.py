def test_add_book(sample_library, book4):
    """Проверка добавления книги."""
    initial_count = len(sample_library.books)
    sample_library.add_book(book4)
    assert len(sample_library.books) == initial_count + 1
    assert sample_library.books[-1].title == "Moby Dick"


def test_delete_book(sample_library):
    """Проверка удаления книги по ID."""
    book_to_delete = sample_library.books[0]
    sample_library.delete_book(book_to_delete.id)
    assert all(book.id != book_to_delete.id for book in sample_library.books)


def test_delete_nonexistent_book(sample_library, capsys):
    """Проверка удаления книги с несуществующим ID."""
    sample_library.delete_book(9999)  # ID, которого нет
    captured = capsys.readouterr()
    assert "Книги с id=9999 нет в библиотеке" in captured.out


def test_change_book_status(sample_library):
    """Проверка изменения статуса книги."""
    book_to_change = sample_library.books[0]
    sample_library.change_book_status(book_to_change.id, "выдана")
    assert sample_library.books[0].status == "выдана"


def test_change_status_nonexistent_book(sample_library, capsys):
    """Проверка изменения статуса несуществующей книги."""
    sample_library.change_book_status(9999, "выдана")
    captured = capsys.readouterr()
    assert "Книги с id=9999 нет в библиотеке" in captured.out


def test_search_book_by_title(sample_library, capsys):
    """Проверка поиска книги по названию."""
    sample_library.search_book("1984")
    captured = capsys.readouterr()
    assert "1984" in captured.out


def test_search_book_by_author(sample_library, capsys):
    """Проверка поиска книги по автору."""
    sample_library.search_book("Harper Lee")
    captured = capsys.readouterr()
    assert "To Kill a Mockingbird" in captured.out


def test_search_book_by_year(sample_library, capsys):
    """Проверка поиска книги по году."""
    sample_library.search_book("1925")
    captured = capsys.readouterr()
    assert "The Great Gatsby" in captured.out


def test_search_nonexistent_book(sample_library, capsys):
    """Проверка поиска книги, которой нет в библиотеке."""
    sample_library.search_book("Nonexistent Book")
    captured = capsys.readouterr()
    assert "Книг по вашему запросу не найдено" in captured.out


def test_get_books_list(sample_library):
    """Проверка получения списка книг."""
    books_list = sample_library.get_books_list()
    assert len(books_list) == len(sample_library.books)
    assert books_list[0]["title"] == "1984"


def test_add_books_from_list(capsys, sample_library):
    """Проверка добавления книг из списка словарей."""
    new_books = [
        {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    ]
    sample_library.add_books_from_list(new_books)
    assert len(sample_library.books) == 5  # Было 3, добавили 2
    assert sample_library.books[-1].title == "The Catcher in the Rye"
    sample_library.print_all_book()
    captured = capsys.readouterr()
    assert (
        f'{("#" + " " * 5)[:5]} | {("Название" + " " * 30)[:30]} | {("Автор" + " " * 15)[:15]} | Год  | Статус'
        in captured.out
    )


def test_str(capsys, sample_library):
    """Проверка вывода информации о библиотеке"""
    print(sample_library)
    captured = capsys.readouterr()
    assert "В библиотеке содержится 3 книг(и)" in captured.out
