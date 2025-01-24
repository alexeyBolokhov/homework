# Задача "Ошибка эволюции"
import random

import ramdom
class Animal:
    # атрибуты
    live = True
    sound = None  # звук
    _DEGREE_OF_DANGER = 0  # степень опастности
    # Объект этого класса обладает следующими атрибутами
    def __init__(self, speed):
        self._cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed # скорость передвижения существа (определяется при создании объекта)

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed # меняем  кооординаты в _cords на dx и множитель speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def attack(self):
        if self._DEGREE_OF_DANGER < 5: # если степень опасности меньше 5
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    # def speak(self):
    #     print(self.sound)  # выводит строку со звуком sound

    def get_cords(self):
        print(f'X:  {self._cords [0]} ,Y: {self._cords [1]}, Z: {self._cords [2]}')
class Bird(Animal):
    beak = True # клюв есть
    def lay_eggs(self):
        num_of_eggs = random.randint(1,4)
        print (f"Here are(is) {num_of_eggs} eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        # new_z = self._cords[2] - abs(dz) * .5 * self.speed # всегда уменьшать координату z (_cords[2] )
        # self._cords[2] = max(new_z, 0) ######
        self._cords[2] = abs(int(self._cords[2]) // int(self.speed)) - dz // 2 # целочисленное делние //

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click" # утконос - атрибут
    def __init__(self, speed):
        super().__init__(speed) # super() используется для вызова методов родительского класса из дочернего, обеспечивая доступ к его функционалу без необходимости дублирования кода
    def speak(self):
        print(self.sound) # выводит строку со звуком sound
#########
db = Duckbill(10)
#print(random.randint(1,4))
print(db.live)
print(db.beak)
db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()