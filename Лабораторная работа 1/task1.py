class Cake:
    def __init__(self, taste: str, shelf_life: int, color: str):
        if not isinstance(color, str):
            raise TypeError('Название цвета должно быть типа str')
        self.color = color
        if shelf_life >= 10:
            raise TypeError('Срок годности слишком большой!')
        self.shelf_life = shelf_life
        if not isinstance(taste):
            raise TypeError('Безвкусный торт это грустно!')
        self.taste = taste
    def absent(self):
        print('Торта нет в магазине')
        self.availability = 0

class Rocket:
    def __init__(self, model_roc: str, capacity: int, turbines):
        if not isinstance(model_roc, str):
            raise TypeError('Название модели ракеты должно быть типа str')
        self.model_roc = model_roc
        if not capacity > 2:
            raise ValueError('Ракета должна вмешать 3 пассажиров')
        self.capacity = capacity
        if turbines > 6:
            raise ValueError('У ракеты не больше шести турбин')
        self.turbines = turbines

class Socks:
    def __init__(self, size: int, colour: str):
        if not isinstance(size, int):
            raise TypeError('Нужны носки определенного размера')
        if size <= 0:
            raise ValueError('Не может быть безразмерных носков')
        self.size = size
        if not isinstance(colour, str):
            raise ValueError('Цвет носков нужно записывать буквами')
        self.colour = colour

if __name__ == "__main__":
    Медовик = Cake('Медовый', 5, 'Песочный')
    Калибр = Rocket('Sizzler', 4, 0)
    Носки = (40, 'белые')
    import doctest
    doctest.testmod()
    pass