class BaseFlowers:
    """Создание и подготовка к работе базового класса Цветы"""
    def __init__(self, name: str, size: float, purpose: list):
        """
        :param name: название цветка
        :param size: высота цветка
        :param purpose: назначение цветка
        """
        self.name = name
        self.size = size
        self.purpose = purpose

    @property
    def name(self):
        """Создание геттера для атрибута name"""
        return self._name

    @name.setter
    def name(self, name: str):
        """Создание cеттера для атрибута name с проверкой name на то, что он состоит из 1-15 букв"""
        if not name.isalpha():
            raise TypeError("Имя должно состоять из букв!")
        if len(name) > 15:
            raise ValueError("Длина имени должна не превышать 15 букв!")
        self._name = name

    @property
    def size(self):
        """Создание геттера для атрибута size"""
        return self._size

    @size.setter
    def size(self, size: float):
        """Создание cеттера для атрибута size с проверкой size на то, что он является положительным числом с
        плавающей точкой, не большим 1"""
        if not isinstance(size, float):
            raise TypeError("Высота цветка должна быть типа float!")
        if size <= 0 or size > 1:
            raise ValueError("Высота цветка должна быть положительной величиной и не превышать 1 м!")
        self._size = size

    @property
    def purpose(self):
        """Создание геттера для атрибута purpose"""
        return self._purpose

    @purpose.setter
    def purpose(self, purpose: list):
        """Создание cеттера для атрибута purpose с проверкой purpose на то, что он является одной из заданных в
        списке purposes строк"""
        purposes = ['декоративный', 'комнатный', 'садовый', 'плодовые']
        if purpose not in purposes:
            raise ValueError("Неверное назначение!")
        self._purpose = purpose

    def __str__(self) -> str:
        """Создание метода, выводящего информацию о цветке в читаемом формате"""
        return f"Цветок: {self._name}. Высота цветка: {self._size} м. Назначение: {self._purpose}."

    def __repr__(self) -> str:
        """Создание метода, выводящего «официальный» текстовый образ объекта, который можно использовать для
        воссоздания этого объекта"""
        return f"{self.__class__.__name__}(name={self._name!r}, size={self._size!r}, purpose={self._purpose})"

    def size_in_feet(self) -> float:
        """Создание метода, переводящего значение высоты цветка size из метров в сантиметры"""
        return self.size * 100



class Rose(BaseFlowers):
    """Создание и подготовка к работе производного класса Роза"""
    def __init__(self, name: str, size: float, purpose: list):
        """
        :param name: наследуется от базового класса Цветы
        :param size: наследуется от базового класса Цветы
        :param purpose: наследуется от базового класса Цветы
        """
        super().__init__(name, size, purpose)

    def capitalize_name(self) -> str:
        """Перегрузка метода, переводящего имя цветка name в слово, начинающееся с заглавной буквы с последующими
        строчными буквами. Теперь метод переводит имя цветка name в слово, состоящее из одних заглавных букв. Это
        сделано с целью визуального выделения декоративных цветов среди других"""
        return self.name.upper()


class Hydrangea(BaseFlowers):
    """Создание и подготовка к работе производного класса Гортензия"""
    def __init__(self, name: str, size: float, purpose: list, tail_length: float):
        """
        :param name: наследуется от базового класса Цветы
        :param size: наследуется от базового класса Цветы
        :param purpose: наследуется от базового класса Цветы
        :param tail_length: длина цветка в метрах
        """
        super().__init__(name, size, purpose)
        self.tail_length = tail_length

    @property
    def tail_length(self):
        """Создание геттера для атрибута tail_length"""
        return self._tail_length

    @tail_length.setter
    def tail_length(self, tail_length: float):
        """Создание cеттера для атрибута tail_length с проверкой tail_length на то, что он является положительным
        числом с плавающей точкой, не большим 1"""
        if not isinstance(tail_length, float):
            raise TypeError("Длина цветка должна быть типа float!")
        if tail_length <= 0 or tail_length > 1:
            raise ValueError("Высота цветка должна быть положительной величиной и не превышать 1 м!")
        self._tail_length = tail_length



    def __str__(self) -> str:
        """Перегрузка метода, выводящего информацию о цветке в читаемом строковом формате, так как в вывод
        добавляется новый параметр: tail_length"""
        return f"Цветы: {self._name}. Высота цветка: {self._size} м. Назначение: {self._purpose}. " \
               f"Высота цветка: {self._tail_length} м."

    def __repr__(self) -> str:
        """Перегрузка метода, выводящего «официальный» текстовый образ объекта, который можно использовать для
        воссоздания этого объекта, так как в вывод добавляется новый параметр: tail_length"""
        return f"{self.__class__.__name__}(name={self._name!r}, size={self._size!r}, purpose={self._purpose!r}, " \
               f"tail_length={self._tail_length!r}"

    def capitalize_name(self) -> str:
        """Перегрузка метода, переводящего имя цветка name в слово, начинающееся с заглавной буквы с последующими
        строчными буквами. Теперь метод переводит имя цветка name в слово, состоящее из одних заглавных букв. Это
        сделано с целью визуального выделения декоративных цветов среди других"""
        return self.name.upper()


flower1 = Rose('кустовая', 0.9, 'декоративный')
flower2 = Hydrangea('Голубая', 0.2, 'комнатный', 0.4)

print(flower1.__str__())
print(flower1.__repr__())
print(round(flower1.size_in_feet(), 2), flower1.capitalize_name())

print()

print(flower2.__str__())
print(flower2.__repr__())
print(round(flower1.size_in_feet(), 2), flower2.capitalize_name())
