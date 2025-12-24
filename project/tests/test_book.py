import sys
from pathlib import Path

# Добавляем корневую директорию проекта в путь для импортов
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from src.book import Book


def test_book_creation():
    """Тест создания книги с корректными параметрами."""
    book = Book(
        title="Война и мир",
        author="Лев Толстой",
        year=1869,
        genre="Роман",
        isbn="978-5-17-123456-7",
    )
    
    assert book.title == "Война и мир"
    assert book.author == "Лев Толстой"
    assert book.year == 1869
    assert book.genre == "Роман"
    assert book.isbn == "978-5-17-123456-7"


def test_book_attributes():
    """Тест проверки всех атрибутов книги."""
    book = Book(
        title="Преступление и наказание",
        author="Фёдор Достоевский",
        year=1866,
        genre="Роман",
        isbn="978-5-17-789012-3",
    )
    
    assert isinstance(book.title, str)
    assert isinstance(book.author, str)
    assert isinstance(book.year, int)
    assert isinstance(book.genre, str)
    assert isinstance(book.isbn, str)


def test_book_different_books():
    """Тест создания разных книг с разными данными."""
    book1 = Book(
        title="Книга 1",
        author="Автор 1",
        year=2000,
        genre="Жанр 1",
        isbn="111-1111111-111-1",
    )
    
    book2 = Book(
        title="Книга 2",
        author="Автор 2",
        year=2010,
        genre="Жанр 2",
        isbn="222-2222222-222-2",
    )
    
    assert book1.title != book2.title
    assert book1.author != book2.author
    assert book1.year != book2.year
    assert book1.genre != book2.genre
    assert book1.isbn != book2.isbn

