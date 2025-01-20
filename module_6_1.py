# Задача "Съедобное, несъедобное":
class Animal: # Животное
    def __init__(self, name: str, alive = True, fed = False): # живой и голодный поумолчанию
        # Атриубты:
        self.alive = alive # живой
        self.fed = fed # накормленный
        self.name = name #  индивидуальное название каждого животного
####### это будет унаследованно
    def eat(self, food):  # food - это параметр, принимающий объекты классов растений
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Plant: # растение
    def __init__(self, name: str, edible = False): # не сЪедобный по умолчанию
        # Атриубты:
        self.edible = edible # съедобность
        self.name = name  # индивидуальное название каждого растения
# наследники
class Mammal(Animal): # Млекопитающее
    pass
    # def eat(self, food): # food - это параметр, принимающий объекты классов растений
    #     if food.edible:
    #         print(f'{self.name} съел {food.name}')
    #         self.fed = True
    #     else:
    #         print(f'{self.name} не стал есть {food.name}')
    #         self.alive = False
class Predator(Animal):
    pass# Хищник
    # def eat(self, food): # food - это параметр, принимающий объекты классов растений
    #     if food.edible:
    #         print(f'{self.name} съел {food.name}')
    #         self.fed = True
    #     else:
    #         print(f'{self.name} не стал есть {food.name}')
    #         self.alive = False
class Flower(Plant):
    pass# Цветок
    #edible = False
class Fruit(Plant): # фрукт
    def __init__(self, name):
        super().__init__(name) # У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
        self.edible = True
# проверка
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)