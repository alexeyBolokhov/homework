# 5_1 Атрибуты и методы объекта
class House:
    def __init__(self, name, number_of_floors):
        self.name = name # атрибут имя
        self.number_of_floors = number_of_floors # атрибут кол-во этажей
        #self.go_to()
    def go_to(self,new_floor): # метод 
       
        self.new_floor = new_floor # атрибут новый этаж
        if new_floor > self.number_of_floors or new_floor < 1: # проверка вдруг больше этаж
            print('Такого этажа не существует')
        else:
            for i in range(1,new_floor+1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name,h1.number_of_floors)
print(h2.name,h2.number_of_floors)
h1.go_to(5)
h2.go_to(10)
h2.go_to(0)
