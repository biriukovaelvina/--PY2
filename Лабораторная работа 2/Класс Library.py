BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """Создание и подготовка к работе класса Книга"""
    def __init__(self, id_: int, name: str, pages: int):
        """
        :param id_: идентификационный номер книги
        :param name: название книги
        :param pages: количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Создание метода, выводящего информацию о книге в удобочитаемом формате"""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Создание метода, выводящего «официальный» текстовый образ книги, который можно использовать для
        воссоздания этой книги"""
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    """Создание и подготовка к работе класса Библиотека"""
    def __init__(self, books: list = None):
        """
        :param books: список книг в библиотеке
        """
        self.books = [] if books is None else books

    def get_next_book_id(self):
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку"""
        if not self.books:
            """Если книг нет, возвращает 1"""
            return 1
        else:
            """Если книги есть, возвращает идентификатор последней книги, увеличенный на 1"""
            return BOOKS_DATABASE[-1].get("id") + 1

    @staticmethod
    def get_index_by_book_id(id_: int):
        """Метод, возвращающий индекс книги в списке"""
        for index, dict_ in enumerate(BOOKS_DATABASE):
            """Если книга существует, возвращается индекс"""
            if "id" in dict_ and dict_["id"] == id_:
                return index
            else:
                """Если книги нет, вызывается ошибка"""
                raise ValueError('Книги с запрашиваемым id не существует')





if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
