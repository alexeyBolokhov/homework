# Задание "Средний балл":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
########
# отдельно для каждого
a = (len(grades[0])) # сколько оценок
b = (sum(grades[0])) # сумма оценок
average = b/a # средний балл
print(average)
########
#print(sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[0]))
#  в одну строку список вычислений среднего
average_list = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[0])]
print(average_list) # список из средних
my_list = list(students) # преобразуем множество в спислк студентов
my_list.sort()  # сортируем список студентов
#print(my_list.sort())
print(my_list)
my_dict = {} # пустой словарь
my_dict.update({my_list[0]: average_list[0], my_list[1]: average_list[1], my_list[2]: average_list[2], my_list[3]: average_list[3], my_list[4]: average_list[4]})
print(my_dict)