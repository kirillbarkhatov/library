import pytest

from src.book import Book
from src.library import Library

# Корректные экземпляры Book

@pytest.fixture
def book1():
    return Book(title="1984", author="George Orwell", year=1949)


@pytest.fixture
def book2():
    return Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960)


@pytest.fixture
def book3():
    return Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)


@pytest.fixture
def book4():
    return Book(title="Moby Dick", author="Herman Melville", year=1851)


@pytest.fixture
def book5():
    return Book(title="War and Peace", author="Leo Tolstoy", year=1869)


@pytest.fixture
def book_dict():
    return {
        "_Book__id": 22,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "year": 1869,
        "_Book__status": "выдана"
    }