immutable_var = (24, 11, 'год', 'месяц') # кортеж ()
print(immutable_var)
print(type(immutable_var))
#####
#immutable_var[1] = 10 # хотим поменять (11 на 10) в кортеже
#print(immutable_var)  # будет ошибка
# кортеж - неизменяемый
#####
mutable_list = [24, 11, 'год', 'месяц'] # список []
print(mutable_list)
print(type(mutable_list))
mutable_list[3] = 'зима' # хотим поменять (месяц на зима) в списке
print(mutable_list)
#список - можно менять
#########
mutable_list.append(2024) # добавили в конец
print(mutable_list)
mutable_list.extend(['река',88,'озеро']) # добавили другим методом (элементы  в [ ] )
print(mutable_list)
mutable_list.extend('озеро') # в отдельные символя разобрал и добавил в конец
print(mutable_list)
print('лужа' in mutable_list) # является ли Лужа элементом списка?
##########
immutable_var = ([24, 11], 'год', 'месяц') # кортеж внутри которого элеиентом явлется список []
immutable_var[0][1] = 9999 # т.к. первый элеиент кортежа список - его элементы можно поменять
print(immutable_var)
print('месяц' in immutable_var) # является ли месяц элементом кортежа?
print(immutable_var.__sizeof__()) #размер
