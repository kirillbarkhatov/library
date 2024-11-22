import pytest

from src.book import Book
from tests.conftest import book1


def test_book_create_success(book1, book2, book3, book4, book5):

    assert book1.title == "1984"
    assert book2.author == "Harper Lee"
    assert book3.year == 1925
    assert not book4.id
    assert book5.status == "в наличии"


invalid_type_book_data = [
    (123, "George Orwell", 1949),         # Неверный тип для title
    ("1984", None, 1949),                 # None вместо строки для author
    ("1984", "George Orwell", "1949"),    # Неверный тип для year (str вместо int)
    ("1984", "George Orwell", None),      # None вместо целого числа для year
    ("", "George Orwell", 1949),
    ("1984", "", 1949),
]


@pytest.mark.parametrize("title,author,year", invalid_type_book_data)
def test_type_invalid_books(title, author, year):
    with pytest.raises(TypeError):
        Book(title=title, author=author, year=year)


invalid_value_book_data = [
    ("1984", "George Orwell", -1),
    ("1984", "George Orwell", 3334),
]


@pytest.mark.parametrize("title,author,year", invalid_value_book_data)
def test_value_invalid_books(title, author, year):
    with pytest.raises(ValueError):
        Book(title=title, author=author, year=year)


def test_book_methods(capsys, book1, book_dict):
    # вывод __str__
    print(book1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "None  | 1984                           | George Orwell   | 1949 | в наличии"

    # сеттер id
    book1.id = 1
    assert book1.id == 1

    # сеттер status
    book1.status = "выдана"
    assert book1.status == "выдана"

    book1.status = "Супер-Пупер-Книга"
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Введите корректный статус: "в наличии" или "выдана"'

    # книга из словаря
    book = Book.from_dict(book_dict)
    assert not book.id
    assert book.title == "War and Peace"
    assert book.author == "Leo Tolstoy"
    assert book.year == 1869
    assert book.status == "выдана"