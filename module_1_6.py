# словари
my_dict = {'Alex' : 'al@mail.com', 'Petr' : 'pet@gmail.com'}
print(my_dict)
print(type(my_dict))
print(my_dict['Alex'])
print(my_dict.get('Vadim','нет ключа'))
my_dict.update({'Volodya': 'vl@mail.com',
                'Ivan': 'ivan@gmail.com'})
print(my_dict)
a = my_dict.pop('Petr')
print('удален: ',a)
print(my_dict)
#############
print('---------------')
# множества
my_set = {1, 2, 3, 'снег' , 1, 2, 3, 'снег', 5, 6, 'дождь'}
print(my_set) # на экране будут уникальные значения
print(my_set.add(8)) #добавляем
print(my_set.add('ветер')) #добавляем
print(my_set.discard('снег')) #удаляем
print(my_set)
