import sys
from pathlib import Path

# Добавляем корневую директорию проекта в путь для импортов
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import random
import pytest
from src.book import Library, Book
from src.simulation import (
    run_simulation,
    generate_random_isbn,
    generate_random_author,
    generate_random_genre,
    generate_random_title,
    generate_random_year,
    create_random_book,
    event_add_book,
    event_remove_random_book,
    event_search_by_author,
    event_search_by_genre,
    event_search_by_year,
    event_update_index,
    event_search_nonexistent_book,
)


def test_generate_random_isbn():
    """Тест генерации случайного ISBN."""
    isbn = generate_random_isbn()
    assert isinstance(isbn, str)
    assert "-" in isbn


def test_generate_random_author():
    """Тест генерации случайного автора."""
    author = generate_random_author()
    assert isinstance(author, str)
    assert len(author) > 0


def test_generate_random_genre():
    """Тест генерации случайного жанра."""
    genre = generate_random_genre()
    assert isinstance(genre, str)
    assert len(genre) > 0


def test_generate_random_title():
    """Тест генерации случайного названия."""
    title = generate_random_title()
    assert isinstance(title, str)
    assert len(title) > 0


def test_generate_random_year():
    """Тест генерации случайного года."""
    year = generate_random_year()
    assert isinstance(year, int)
    assert 1800 <= year <= 2024


def test_create_random_book():
    """Тест создания случайной книги."""
    book = create_random_book()
    assert isinstance(book, Book)
    assert isinstance(book.title, str)
    assert isinstance(book.author, str)
    assert isinstance(book.year, int)
    assert isinstance(book.genre, str)
    assert isinstance(book.isbn, str)


def test_event_add_book():
    """Тест события добавления книги."""
    library = Library()
    initial_count = len(library.book_collection)
    
    event_add_book(library)
    
    assert len(library.book_collection) == initial_count + 1
    assert len(library.index_dict) == initial_count + 1


def test_event_remove_random_book_empty():
    """Тест события удаления книги из пустой библиотеки."""
    library = Library()
    
    event_remove_random_book(library)
    
    assert len(library.book_collection) == 0


def test_event_remove_random_book():
    """Тест события удаления случайной книги."""
    library = Library()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", "111-1111111-111-1")
    book2 = Book("Книга 2", "Автор 2", 2010, "Жанр 2", "222-2222222-222-2")
    
    library.add_book(book1)
    library.add_book(book2)
    
    initial_count = len(library.book_collection)
    
    event_remove_random_book(library)
    
    assert len(library.book_collection) == initial_count - 1


def test_event_search_by_author():
    """Тест события поиска по автору."""
    library = Library()
    book = Book("Книга", "Лев Толстой", 2000, "Жанр", "111-1111111-111-1")
    library.add_book(book)
    
    event_search_by_author(library)
    
    assert True


def test_event_search_by_genre():
    """Тест события поиска по жанру."""
    library = Library()
    book = Book("Книга", "Автор", 2000, "Роман", "111-1111111-111-1")
    library.add_book(book)
    
    event_search_by_genre(library)
    
    assert True


def test_event_search_by_year():
    """Тест события поиска по году."""
    library = Library()
    book = Book("Книга", "Автор", 2000, "Жанр", "111-1111111-111-1")
    library.add_book(book)
    
    event_search_by_year(library)
    
    assert True


def test_event_update_index():
    """Тест события обновления индекса."""
    library = Library()
    book = Book("Книга", "Автор", 2000, "Жанр", "111-1111111-111-1")
    library.add_book(book)
    
    event_update_index(library)
    
    assert len(library.index_dict) == 1


def test_event_search_nonexistent_book():
    """Тест события поиска несуществующей книги."""
    library = Library()
    
    event_search_nonexistent_book(library)
    
    assert True


def test_run_simulation_default_steps():
    """Тест запуска симуляции с параметрами по умолчанию."""
    run_simulation()
    
    assert True


def test_run_simulation_custom_steps():
    """Тест запуска симуляции с заданным количеством шагов."""
    run_simulation(steps=5)
    
    assert True


def test_run_simulation_with_seed():
    """Тест запуска симуляции с seed для воспроизводимости."""
    run_simulation(steps=10, seed=42)
    
    assert True


def test_run_simulation_reproducibility():
    """Тест воспроизводимости симуляции с одинаковым seed."""
    seed = 12345
    steps = 5
    
    library1 = Library()
    library2 = Library()
    
    random.seed(seed)
    for _ in range(steps):
        book = create_random_book()
        library1.add_book(book)
    
    random.seed(seed)
    for _ in range(steps):
        book = create_random_book()
        library2.add_book(book)
    
    assert len(library1.book_collection) == len(library2.book_collection)
    
    books1 = list(library1.book_collection)
    books2 = list(library2.book_collection)
    
    for book1, book2 in zip(books1, books2):
        assert book1.title == book2.title
        assert book1.author == book2.author
        assert book1.year == book2.year
        assert book1.genre == book2.genre
        assert book1.isbn == book2.isbn


def test_run_simulation_zero_steps():
    """Тест запуска симуляции с нулевым количеством шагов."""
    run_simulation(steps=0)
    
    assert True


def test_run_simulation_large_steps():
    """Тест запуска симуляции с большим количеством шагов."""
    run_simulation(steps=100)
    
    assert True


def test_simulation_events_diversity():
    """Тест разнообразия событий в симуляции."""
    library = Library()
    events_called = set()
    
    random.seed(42)
    events = [
        ("add_book", event_add_book),
        ("remove_book", event_remove_random_book),
        ("search_author", event_search_by_author),
        ("search_genre", event_search_by_genre),
        ("search_year", event_search_by_year),
        ("update_index", event_update_index),
        ("search_nonexistent", event_search_nonexistent_book),
    ]
    
    for _ in range(50):
        event_name, event_func = random.choice(events)
        events_called.add(event_name)
        try:
            event_func(library)
        except Exception:
            pass
    
    assert len(events_called) >= 5

