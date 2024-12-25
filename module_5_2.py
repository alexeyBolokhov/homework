# 5_2 Атрибуты и методы объекта
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
                
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        str1 = str((f'Название: {self.name} , количество этажей: {self.number_of_floors}'))
        return str1
h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)
# print(h1.name,h1.number_of_floors)
# print(h2.name,h2.number_of_floors)
# h1.go_to(5)
# h2.go_to(10)
# h2.go_to(0)
print(len(h1))
print(len(h2))
print(h1)
print(h2)