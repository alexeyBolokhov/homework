# Задача "Нули ничто, отрицание недопустимо!"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
pos = 0
len_my_list = len(my_list)
while my_list[pos] != len_my_list:
    if my_list[pos] == 0 : # 0 - не отрицательное и не положительное число
        pos = pos + 1 # идем дальше
    elif my_list[pos] > 0: # положительное
         print(my_list[pos]) # выводим
         pos = pos + 1 # идем дальше
    else: break # не больше нуля то стоп
print('зевершено')