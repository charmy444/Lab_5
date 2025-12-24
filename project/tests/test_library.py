import sys
from pathlib import Path

# Добавляем корневую директорию проекта в путь для импортов
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from src.book import Book, Library


def test_library_creation():
    """Тест создания библиотеки."""
    library = Library()
    assert len(library.book_collection) == 0
    assert len(library.index_dict) == 0


def test_library_add_book():
    """Тест добавления книги в библиотеку."""
    library = Library()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    library.add_book(book)
    
    assert len(library.book_collection) == 1
    assert len(library.index_dict) == 1
    assert book in library.book_collection
    assert library.index_dict[book.isbn] == book


def test_library_add_multiple_books():
    """Тест добавления нескольких книг."""
    library = Library()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    
    library.add_book(book1)
    library.add_book(book2)
    
    assert len(library.book_collection) == 2
    assert len(library.index_dict) == 2


def test_library_remove_book():
    """Тест удаления книги из библиотеки."""
    library = Library()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    library.add_book(book)
    library.remove_book(book)
    
    assert len(library.book_collection) == 0
    assert len(library.index_dict) == 0


def test_library_search_by_isbn_found():
    """Тест поиска книги по ISBN (книга найдена)."""
    library = Library()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    library.add_book(book)
    result = library.search_by_isbn("123-4567890-123-4")
    
    assert result is not None
    assert result == book


def test_library_search_by_isbn_not_found():
    """Тест поиска книги по ISBN (книга не найдена)."""
    library = Library()
    result = library.search_by_isbn("999-9999999-999-9")
    
    assert result is None


def test_library_search_by_author_found():
    """Тест поиска книг по автору (книги найдены)."""
    library = Library()
    book1 = Book("Книга 1", "Автор", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор", 2010, "Жанр 2", "222-2222222-222-2")
    book3 = Book("Книга 3", "Другой автор", 2020, "Жанр 3", "333-3333333-333-3")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    results = library.search_by_author("Автор")
    
    assert len(results) == 2
    assert isinstance(results, type(library.book_collection))
    assert book1 in results
    assert book2 in results
    assert book3 not in results


def test_library_search_by_author_not_found():
    """Тест поиска книг по автору (книги не найдены)."""
    library = Library()
    results = library.search_by_author("Несуществующий автор")
    
    assert len(results) == 0
    assert isinstance(results, type(library.book_collection))


def test_library_search_by_year_found():
    """Тест поиска книг по году (книги найдены)."""
    library = Library()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2000, "Жанр 2", "222-2222222-222-2")
    book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", "333-3333333-333-3")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    results = library.search_by_year(2000)
    
    assert len(results) == 2
    assert isinstance(results, type(library.book_collection))
    assert book1 in results
    assert book2 in results
    assert book3 not in results


def test_library_search_by_year_not_found():
    """Тест поиска книг по году (книги не найдены)."""
    library = Library()
    results = library.search_by_year(1900)
    
    assert len(results) == 0
    assert isinstance(results, type(library.book_collection))


def test_library_search_by_title_found():
    """Тест поиска книг по названию (книги найдены)."""
    library = Library()
    book1 = Book("Война и мир", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Война и мир", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    book3 = Book("Другая книга", "Автор 3", 2020, "Жанр 3", "333-3333333-333-3")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    results = library.search_by_title("Война и мир")
    
    assert len(results) == 2
    assert isinstance(results, type(library.book_collection))
    assert book1 in results
    assert book2 in results
    assert book3 not in results


def test_library_search_by_title_not_found():
    """Тест поиска книг по названию (книги не найдены)."""
    library = Library()
    results = library.search_by_title("Несуществующая книга")
    
    assert len(results) == 0
    assert isinstance(results, type(library.book_collection))


def test_library_search_by_genre_found():
    """Тест поиска книг по жанру (книги найдены)."""
    library = Library()
    book1 = Book("Книга 1", "Автор 1", 2000, "Роман", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Роман", "222-2222222-222-2")
    book3 = Book("Книга 3", "Автор 3", 2020, "Детектив", "333-3333333-333-3")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    results = library.search_by_genre("Роман")
    
    assert len(results) == 2
    assert isinstance(results, type(library.book_collection))
    assert book1 in results
    assert book2 in results
    assert book3 not in results


def test_library_search_by_genre_not_found():
    """Тест поиска книг по жанру (книги не найдены)."""
    library = Library()
    results = library.search_by_genre("Несуществующий жанр")
    
    assert len(results) == 0
    assert isinstance(results, type(library.book_collection))


def test_library_update_index():
    """Тест обновления индекса библиотеки."""
    library = Library()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    
    library.add_book(book1)
    library.add_book(book2)
    
    assert len(library.index_dict) == 2
    
    library.update_index()
    
    assert len(library.index_dict) == 2
    assert library.index_dict[book1.isbn] == book1
    assert library.index_dict[book2.isbn] == book2


def test_library_update_index_after_manual_modification():
    """Тест обновления индекса после ручной модификации коллекции."""
    library = Library()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    
    library.add_book(book1)
    library.add_book(book2)
    
    library.book_collection.remove(book1)
    
    library.update_index()
    
    assert len(library.index_dict) == 1
    assert book1.isbn not in library.index_dict.isbn_index
    assert book2.isbn in library.index_dict.isbn_index


def test_library_remove_nonexistent_book():
    """Тест удаления несуществующей книги (должна быть ошибка)."""
    library = Library()
    book = Book("Тест", "Автор", 2000, "Жанр", "123-4567890-123-4")
    
    with pytest.raises(ValueError):
        library.remove_book(book)

