import random
from project.src.book import Library, Book


def generate_random_isbn() -> str:
    return f"{random.randint(100, 999)}-{random.randint(1000000, 9999999)}-{random.randint(100, 999)}-{random.randint(0, 9)}"


def generate_random_author() -> str:
    authors = [
        "Лев Толстой",
        "Фёдор Достоевский",
        "Антон Чехов",
        "Александр Пушкин",
        "Николай Гоголь",
        "Иван Тургенев",
        "Михаил Булгаков",
        "Владимир Набоков",
        "Александр Солженицын",
        "Борис Пастернак",
    ]
    return random.choice(authors)


def generate_random_genre() -> str:
    genres = [
        "Роман",
        "Детектив",
        "Фантастика",
    ]
    genre = random.choice(genres)
    if genre == "Роман":
        return "Исторический роман"
    return genre


def generate_random_title() -> str:
    titles = [
        "Война и мир",
        "Преступление и наказание",
        "Мастер и Маргарита",
        "Анна Каренина",
        "Братья Карамазовы",
        "Идиот",
        "Мёртвые души",
        "Евгений Онегин",
        "Отцы и дети",
        "Обломов",
    ]
    return random.choice(titles)


def generate_random_year() -> int:
    year_str = random.randint(0, 2024)
    if year_str[2:4] == "00":
        return (int(year_str) + 10)
    return int(year_str)

def create_random_book() -> Book:
    return Book(
        title=generate_random_title(),
        author=generate_random_author(),
        year=generate_random_year(),
        genre=generate_random_genre(),
        isbn=generate_random_isbn(),
    )


def event_add_book(library: Library) -> None:
    book = create_random_book()
    library.add_book(book)
    print(f"Добавлена книга: '{book.title}' автора {book.author}")


def event_remove_random_book(library: Library) -> None:
    if len(library.book_collection) == 0:
        print("Нет книг для удаления")
        return
    
    random_book = random.choice(library.book_collection.books)
    library.remove_book(random_book)
    print(f"Удалена книга: '{random_book.title}' автора {random_book.author}")


def event_search_by_author(library: Library) -> None:
    author = generate_random_author()
    results = library.search_by_author(author)
    print(f"Поиск по автору '{author}': найдено {len(results)} книг")


def event_search_by_genre(library: Library) -> None:
    genre = generate_random_genre()
    results = library.search_by_genre(genre)
    print(f"Поиск по жанру '{genre}': найдено {len(results)} книг")


def event_search_by_year(library: Library) -> None:
    year = generate_random_year()
    results = library.search_by_year(year)
    print(f"Поиск по году {year}: найдено {len(results)} книг")


def event_update_index(library: Library) -> None:
    library.update_index()
    print(f"Индекс обновлен. Всего книг в индексе: {len(library.index_dict)}")


def event_search_nonexistent_book(library: Library) -> None:
    nonexistent_isbn = generate_random_isbn()
    book = library.search_by_isbn(nonexistent_isbn)
    if book is None:
        print(f"Попытка найти книгу с ISBN {nonexistent_isbn}: книга не найдена (корректная обработка)")
    else:
        print(f"Неожиданно найдена книга с ISBN {nonexistent_isbn}")


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
    
    library = Library()
    events = [
        ("add_book", event_add_book),
        ("remove_book", event_remove_random_book),
        ("search_author", event_search_by_author),
        ("search_genre", event_search_by_genre),
        ("search_year", event_search_by_year),
        ("update_index", event_update_index),
        ("search_nonexistent", event_search_nonexistent_book),
    ]
    
    print(f"[СИМУЛЯЦИЯ] Начало симуляции библиотеки")
    print(f"[СИМУЛЯЦИЯ] Количество шагов: {steps}")
    if seed is not None:
        print(f"[СИМУЛЯЦИЯ] Seed: {seed}")
    
    for step in range(1, steps):
        event_name, event_func = random.choice(events)
        print(f"[Шаг {step:3d}] Событие: {event_name}")
        try:
            event_func(library)
        except Exception as e:
            print(f"[Шаг {step:3d}] Ошибка при выполнении события: {e}")
        print()
    print(f"[СИМУЛЯЦИЯ] Симуляция завершена")
    print(f"[СИМУЛЯЦИЯ] Всего книг в библиотеке: {len(library.book_collection)}")

