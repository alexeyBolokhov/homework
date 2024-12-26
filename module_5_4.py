# 5_4 Задача "История строительства":
class House:
    houses_history = []
    #__instance = None
    def __new__(cls, *args,**kwargs):
        cls.houses_history.append(args[0]) # имя берем по индексу0 и добавляем в список cls.houses_history
       
        return super().__new__(cls)
        
    def __init__(self, name, number_of_floors):
        self.name = name # атрибут имя
        self.number_of_floors = number_of_floors # атрибут кол-во этажей
        
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
                
    


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2 # удаляется но не из [] списка houses_history
del h3 # удаляется но не из [] спискаhouses_history
print(House.houses_history)