import sys
from pathlib import Path

# Добавляем корневую директорию проекта в путь для импортов
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from src.book import Book, BookCollection


def test_book_collection_creation():
    """Тест создания пустой коллекции книг."""
    collection = BookCollection()
    assert len(collection) == 0
    assert len(collection.books) == 0


def test_book_collection_add():
    """Тест добавления книги в коллекцию."""
    collection = BookCollection()
    book = Book(
        title="Тест",
        author="Автор",
        year=2000,
        genre="Жанр",
        isbn="123-4567890-123-4",
    )
    
    collection.add(book)
    assert len(collection) == 1
    assert collection[0] == book


def test_book_collection_add_multiple():
    """Тест добавления нескольких книг."""
    collection = BookCollection()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    book3 = Book("Книга 3", "Автор 3", 2020, "Жанр 3", "333-3333333-333-3")
    
    collection.add(book1)
    collection.add(book2)
    collection.add(book3)
    
    assert len(collection) == 3
    assert collection[0] == book1
    assert collection[1] == book2
    assert collection[2] == book3


def test_book_collection_remove():
    """Тест удаления книги из коллекции."""
    collection = BookCollection()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    collection.add(book)
    assert len(collection) == 1
    
    collection.remove(book)
    assert len(collection) == 0


def test_book_collection_remove_nonexistent():
    """Тест удаления несуществующей книги (должна быть ошибка)."""
    collection = BookCollection()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    with pytest.raises(ValueError):
        collection.remove(book)


def test_book_collection_iteration():
    """Тест итерации по коллекции."""
    collection = BookCollection()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    
    collection.add(book1)
    collection.add(book2)
    
    books_list = list(collection)
    assert len(books_list) == 2
    assert book1 in books_list
    assert book2 in books_list


def test_book_collection_indexing():
    """Тест индексации коллекции."""
    collection = BookCollection()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    
    collection.add(book1)
    collection.add(book2)
    
    assert collection[0] == book1
    assert collection[1] == book2
    assert collection[-1] == book2


def test_book_collection_slice():
    """Тест среза коллекции."""
    collection = BookCollection()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    book3 = Book("Книга 3", "Автор 3", 2020, "Жанр 3", "333-3333333-333-3")
    
    collection.add(book1)
    collection.add(book2)
    collection.add(book3)
    
    slice_result = collection[0:2]
    assert len(slice_result) == 2
    assert slice_result[0] == book1
    assert slice_result[1] == book2


def test_book_collection_index_out_of_range():
    """Тест обращения к несуществующему индексу."""
    collection = BookCollection()
    
    with pytest.raises(IndexError):
        _ = collection[0]

