class Book:
    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        genre: str,
        isbn: str,
    ) -> None:

        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn


class BookCollection:
    def __init__(self) -> None:
        self.books: list[Book] = []
    
    def __getitem__(self, key: int | slice) -> Book | list[Book]:
        return self.books[key]
    
    def __iter__(self):
        return iter(self.books)
    
    def __len__(self) -> int:
        return len(self.books)
    
    def add(self, book: Book) -> None:
        self.books.append(book)
    
    def remove(self, book: Book) -> None:
        self.books.remove(book)


class IndexDict:
    def __init__(self) -> None:
        self.isbn_index: dict[str, Book] = {}
        self.author_index: dict[str, list[Book]] = {}
        self.year_index: dict[int, list[Book]] = {}
    
    def __getitem__(self, key: str | int) -> Book | list[Book]:
        if isinstance(key, str):
            if key in self.isbn_index:
                return self.isbn_index[key]
            if key in self.author_index:
                return self.author_index[key]
        if isinstance(key, int):
            if key in self.year_index:
                return self.year_index[key]
        raise KeyError(key)
    
    def __iter__(self):
        return iter(self.isbn_index.values())
    
    def __len__(self) -> int:
        return len(self.isbn_index)
    
    def add(self, book: Book) -> None:
        self.isbn_index[book.isbn] = book
        
        if book.author not in self.author_index:
            self.author_index[book.author] = []
        self.author_index[book.author].append(book)
        
        if book.year not in self.year_index:
            self.year_index[book.year] = []
        self.year_index[book.year].append(book)
    
    def remove(self, book: Book) -> None:
        if book.isbn not in self.isbn_index:
            raise KeyError(f"Книга с ISBN {book.isbn} не найдена")
        
        del self.isbn_index[book.isbn]
        
        if book.author in self.author_index:
            self.author_index[book.author].remove(book)
            if not self.author_index[book.author]:
                del self.author_index[book.author]
        
        if book.year in self.year_index:
            self.year_index[book.year].remove(book)
            if not self.year_index[book.year]:
                del self.year_index[book.year]


class Library:
    def __init__(self) -> None:
        self.book_collection: BookCollection = BookCollection()
        self.index_dict: IndexDict = IndexDict()
    
    def add_book(self, book: Book) -> None:
        self.book_collection.add(book)
        self.index_dict.add(book)
    
    def remove_book(self, book: Book) -> None:
        self.book_collection.remove(book)
        self.index_dict.remove(book)
    
    def search_by_isbn(self, isbn: str) -> Book | None:
        try:
            return self.index_dict[isbn]
        except KeyError:
            return None
    
    def search_by_author(self, author: str) -> BookCollection:
        result = BookCollection()
        try:
            books = self.index_dict[author]
            if isinstance(books, list):
                for book in books:
                    result.add(book)
            else:
                result.add(books)
        except KeyError:
            pass
        return result
    
    def search_by_year(self, year: int) -> BookCollection:
        result = BookCollection()
        try:
            books = self.index_dict[year]
            if isinstance(books, list):
                for book in books:
                    result.add(book)
            else:
                result.add(books)
        except KeyError:
            pass
        return result
    
    def search_by_title(self, title: str) -> BookCollection:
        result = BookCollection()
        for book in self.book_collection:
            if book.title == title:
                result.add(book)
        return result
    
    def search_by_genre(self, genre: str) -> BookCollection:
        result = BookCollection()
        for book in self.book_collection:
            if book.genre == genre:
                result.add(book)
        return result
    
    def update_index(self) -> None:
        """
        Обновляет индекс на основе текущей коллекции книг.
        Пересоздает все индексы заново.
        """
        self.index_dict = IndexDict()
        for book in self.book_collection:
            self.index_dict.add(book)

