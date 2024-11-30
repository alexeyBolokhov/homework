# Задача "Рекурсивное умножение цифр"
def get_multiplied_digits(n):
    str_number =str(n)
    # При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
    first = int(str_number[0])
    #if first == 0:
    print(f'first: {first} len(str_number): {len(str_number)}') # для сверки
    if len(str_number) > 1 :
        return first * get_multiplied_digits(int(str_number[1:]))

    else:
        return first

result = get_multiplied_digits(40203) # все ок
print(result)
result2 = get_multiplied_digits(402030) # а вот если в конце 0, то никак
print(result2)