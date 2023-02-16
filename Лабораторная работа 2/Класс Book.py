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


if __name__ == '__main__':
    """Инициализация списка книг"""
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        """Проверка метода __str__"""
        print(book)

    """Проверка метода __repr__"""
    print(list_books)








