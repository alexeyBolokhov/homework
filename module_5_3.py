# 5_3 Атрибуты и методы объекта, Перегрузка операторов
class House:
    def __init__(self, name, number_of_floors):
        self.name = name # атрибут имя
        self.number_of_floors = number_of_floors # атрибут кол-во этажей
        #self.go_to()
    # def go_to(self,new_floor): # метод 
       
    #     self.new_floor = new_floor # атрибут новый этаж
    #     if new_floor > self.number_of_floors or new_floor < 1: # проверка вдруг больше этаж
    #         print('Такого этажа не существует')
    #     else:
    #         for i in range(1,new_floor+1):
    #             print(i)
                
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        str1 = str((f'Название: {self.name} , количество этажей: {self.number_of_floors}'))
        return str1
    def __eq__(self, other): # ==
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else: return NotImplemented
    def __add__(self, value):
        if isinstance(value, (int)):
            return House(self.name, self.number_of_floors + value) 
        else: return print('не целое INT') 
            # h1 = h1 + 10 можно
            # но h1 = 10 + h1 нельзя
    def __radd__(self, other):
        return self.__add__(other) # теперь h1 = 10 + h1 можно
    
    def __iadd__(self, other):
        self.number_of_floors += other # x += y эквивалентно x = x + y
        return self
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)  
    def __gt__(self, other): # (>)
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else: return NotImplemented
    def __ge__(self, other): # (>=)
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else: return NotImplemented
    def __lt__(self, other): # (<)
        if isinstance(other,House):
            return self.number_of_floors < other.number_of_floors
        else: return NotImplemented
    def __le__(self, other): # (<=)
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else: return NotImplemented
    def __ne__(self, other): # (!=)
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else: return NotImplemented
h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(f'eq1 {h1 == h2}') # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(f'eq2 {h1 == h2}')

h2 = 10 + h2 # __radd__
print(h2)

h1 += 10 # __iadd__
print(h1)
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__