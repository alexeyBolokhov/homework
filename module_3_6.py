# b = ''
# print(isinstance(b, str))

# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
def calculate_structure_sum(*arg):
    #print(arg)

    summator = 0 #
    #List список , Dict словарь {}, Set множество , Tuple картеж
    for i in arg:
        #print(i)

        if isinstance(i, str):
            #print(f'::str: {len(i)}')  # для сверки
            summator += len(i) # в цикле суммируется

        if isinstance(i, int):
            summator += i # в цикле суммируется
        if isinstance(i, float):
            summator += i # в цикле суммируется

        if isinstance(i, list):
            summator += calculate_structure_sum(*i) #рекурсивно

        if isinstance(i, dict):
            elem_dict = tuple(i.items()) # надо преобразовать без него не перебрать элементы словаря
            summator += calculate_structure_sum(*elem_dict) #рекурсивно

        if isinstance(i, tuple):
            summator += calculate_structure_sum(*i) #рекурсивно

        if isinstance(i, set):
            summator += calculate_structure_sum(*i) #рекурсивно


    return summator



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)

print(result)