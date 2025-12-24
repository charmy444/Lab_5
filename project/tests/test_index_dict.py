import sys
from pathlib import Path

# Добавляем корневую директорию проекта в путь для импортов
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from src.book import Book, IndexDict


def test_index_dict_creation():
    """Тест создания пустого индекса."""
    index = IndexDict()
    assert len(index) == 0
    assert len(index.isbn_index) == 0
    assert len(index.author_index) == 0
    assert len(index.year_index) == 0


def test_index_dict_add_book():
    """Тест добавления книги в индекс."""
    index = IndexDict()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    index.add(book)
    
    assert len(index) == 1
    assert index.isbn_index[book.isbn] == book
    assert book in index.author_index[book.author]
    assert book in index.year_index[book.year]


def test_index_dict_add_multiple_books_same_author():
    """Тест добавления нескольких книг одного автора."""
    index = IndexDict()
    book1 = Book("Книга 1", "Автор", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор", 2010, "Жанр 2", "222-2222222-222-2")
    
    index.add(book1)
    index.add(book2)
    
    assert len(index) == 2
    assert len(index.author_index["Автор"]) == 2
    assert book1 in index.author_index["Автор"]
    assert book2 in index.author_index["Автор"]


def test_index_dict_add_multiple_books_same_year():
    """Тест добавления нескольких книг одного года."""
    index = IndexDict()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2000, "Жанр 2", "222-2222222-222-2")
    
    index.add(book1)
    index.add(book2)
    
    assert len(index.year_index[2000]) == 2
    assert book1 in index.year_index[2000]
    assert book2 in index.year_index[2000]


def test_index_dict_get_by_isbn():
    """Тест получения книги по ISBN."""
    index = IndexDict()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    index.add(book)
    result = index[book.isbn]
    
    assert result == book
    assert isinstance(result, Book)


def test_index_dict_get_by_author():
    """Тест получения книг по автору."""
    index = IndexDict()
    book1 = Book("Книга 1", "Автор", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор", 2010, "Жанр 2", "222-2222222-222-2")
    
    index.add(book1)
    index.add(book2)
    
    result = index["Автор"]
    assert isinstance(result, list)
    assert len(result) == 2
    assert book1 in result
    assert book2 in result


def test_index_dict_get_by_year():
    """Тест получения книг по году."""
    index = IndexDict()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2000, "Жанр 2", "222-2222222-222-2")
    
    index.add(book1)
    index.add(book2)
    
    result = index[2000]
    assert isinstance(result, list)
    assert len(result) == 2
    assert book1 in result
    assert book2 in result


def test_index_dict_get_nonexistent_isbn():
    """Тест получения несуществующей книги по ISBN."""
    index = IndexDict()
    
    with pytest.raises(KeyError):
        _ = index["999-9999999-999-9"]


def test_index_dict_get_nonexistent_author():
    """Тест получения книг несуществующего автора."""
    index = IndexDict()
    
    with pytest.raises(KeyError):
        _ = index["Несуществующий автор"]


def test_index_dict_get_nonexistent_year():
    """Тест получения книг несуществующего года."""
    index = IndexDict()
    
    with pytest.raises(KeyError):
        _ = index[1900]


def test_index_dict_remove_book():
    """Тест удаления книги из индекса."""
    index = IndexDict()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    index.add(book)
    assert len(index) == 1
    
    index.remove(book)
    assert len(index) == 0
    assert book.isbn not in index.isbn_index
    assert book.author not in index.author_index
    assert book.year not in index.year_index


def test_index_dict_remove_book_with_multiple_same_author():
    """Тест удаления книги при наличии нескольких книг одного автора."""
    index = IndexDict()
    book1 = Book("Книга 1", "Автор", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор", 2010, "Жанр 2", "222-2222222-222-2")
    
    index.add(book1)
    index.add(book2)
    
    index.remove(book1)
    
    assert len(index) == 1
    assert book1.isbn not in index.isbn_index
    assert book2.isbn in index.isbn_index
    assert len(index.author_index["Автор"]) == 1
    assert book2 in index.author_index["Автор"]


def test_index_dict_remove_last_book_of_author():
    """Тест удаления последней книги автора (ключ должен удалиться)."""
    index = IndexDict()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    index.add(book)
    index.remove(book)
    
    assert "Автор" not in index.author_index


def test_index_dict_remove_last_book_of_year():
    """Тест удаления последней книги года (ключ должен удалиться)."""
    index = IndexDict()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    index.add(book)
    index.remove(book)
    
    assert 2000 not in index.year_index


def test_index_dict_remove_nonexistent_book():
    """Тест удаления несуществующей книги (должна быть ошибка)."""
    index = IndexDict()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    with pytest.raises(KeyError):
        index.remove(book)


def test_index_dict_iteration():
    """Тест итерации по индексу."""
    index = IndexDict()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    
    index.add(book1)
    index.add(book2)
    
    books_list = list(index)
    assert len(books_list) == 2
    assert book1 in books_list
    assert book2 in books_list

