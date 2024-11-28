# Задача "Распаковка"
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
    return
###
values_list = [88, 'hello', False]
values_dict = {'a': 777, 'b': 'banan', 'c': False}
values_list_2 = [857189,'Password']
###
print_params(b = 25)
print_params(c = [1,2,3])
###
print_params(*values_list) #распаковка параметров * для списка
print_params(**values_dict) #распаковка параметров ** для словаря
###
print_params(*values_list_2, 42)