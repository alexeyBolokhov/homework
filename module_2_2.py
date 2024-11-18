# Задача "Все ли равны?":
first = int(input("Введите 1-е число: "))
second = int(input("Введите 2-е число: "))
third = int(input("Введите 3-е число: "))
if first == second and first == third: # все 3 одинаковые (1й равен 2 и 1й равен 3)
    print(3)
elif first == second or first == third  or second == third : # достаточно выполнить одно из трех условий (любые два равны)
    print(2)
else:
    print(0)