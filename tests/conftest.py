import pytest

from src.book import Book
from src.library import Library

# Корректные экземпляры Book

@pytest.fixture
def book1():
    """Фикструра книги для тестов"""
    return Book(title="1984", author="George Orwell", year=1949)


@pytest.fixture
def book2():
    """Фикструра книги для тестов"""
    return Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960)


@pytest.fixture
def book3():
    """Фикструра книги для тестов"""
    return Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)


@pytest.fixture
def book4():
    """Фикструра книги для тестов"""
    return Book(title="Moby Dick", author="Herman Melville", year=1851)


@pytest.fixture
def book5():
    """Фикструра книги для тестов"""
    return Book(title="War and Peace", author="Leo Tolstoy", year=1869)


@pytest.fixture
def book_dict():
    """Фикстура словаря с книгой"""
    return {
        "_Book__id": 22,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "year": 1869,
        "_Book__status": "выдана"
    }


@pytest.fixture
def sample_library():
    """Фикстура с библиотекой и несколькими книгами для тестов."""
    library = Library("Test Library")
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
    return library


@pytest.fixture
def library_data():
    """Фикстура для данных библиотеки."""
    return [
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    ]