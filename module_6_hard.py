# Они все так похожи
class Figure:
    sides_count = 0  # Количество сторон фигуры (по умолчанию 0 для базового класса)

    def __init__(self, color, *sides):
        self.__sides = []  # Инициализируем инкапсулированный атрибут для сторон
        self.__color = list(color)  # Сохраняем цвет в формате RGB как список
        self.filled = False  # Устанавливаем, закрашена ли фигура

    def get_color(self):
        #Возвращает текущий цвет
        return self.__color  # Возвращаем список RGB цветов

    def __is_valid_color(self, r, g, b):
        # Проверяем, что все значения - целые числа в диапазоне от 0 до 255
        for i in [r, g, b]:
            if isinstance(i, int) and 0 <= i <= 255:
                return True
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b): # Проверяем корректность цвета
            self.__color = [r, g, b] # Устанавливаем новый цвет

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                # возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим
                if isinstance(side, int) and side > 0:
                    return True
                return False

    def get_sides(self):
        return self.__sides  #Возвращаем список сторон фигуры3

    def __len__(self):
        return sum(self.__sides) #периметр сумма всех сторон

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides): # Проверяем корректность новых сторон
            self.__sides = list(new_sides) # Устанавливаем новые стороны

class Circle(Figure):
    sides_count = 1 # атрибут одна сторона окружность

    def __init__(self, color, length): # Вызываем конструктор родительского класса Figure
        super().__init__(color, length)
        self.__radius = length / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2) # площадь круга
class Triangle(Figure):
    sides_count = 3 # атрибут 3 стороны треугольника

    def __init__(self, color, a, b, c):  # Вызываем конструктор родительского класса Figure с тремя сторонами
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()  # Получаем стороны треугольника
        s = (a + b + c) / 2  # Полупериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12  # У куба двенадцать рёбер

    def __init__(self, color, edge_length):
        super().__init__(color)
        # Устанавливаем все рёбра равными
        self.set_sides(*[edge_length] * self.sides_count)


    def get_volume(self):
        edge_length = self.get_sides()[0] #длинна
        return edge_length ** 3# Объём куба: a^3
########################
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())