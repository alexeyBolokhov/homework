# Задача "Изменять нельзя получать":
class Vehicle: #это любой транспорт
    __COLOR_VARIANTS = ['черный', 'зеленый', 'серый', 'малиновый', 'серо-бур-малиновый'] # это атрибут класса
    def __init__(self, owner: str, model : str, engine_power : int, color : str):
        self.owner = owner # владелец транспорта (может меняться)
        self.__model = model # модель (марка) транспорта (не может меняться)
        self.__engine_power = engine_power # мощность двигателя (не может меняться)
        self.__color = color # название цвета (не может меняться)
# методы
    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец:', self.owner)

    def set_color(self, new_color): # принимает аршумент
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle): # (седан) - наследник класса Vehicle
    __PASSENGERS_LIMIT = 5 # это атрибут класса
# проверка
# Текущие цвета __COLOR_VARIANTS = ['черный', 'зеленый', 'серый', 'малиновый', 'серо-бур-малиновый']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('серый')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()