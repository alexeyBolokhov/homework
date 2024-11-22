#Задача "Матрица воплоти"
### Итооовая в конце, здесь этапы
matrix = []
for i in range(4): # сколько поставим - столько выведет список
    #print(i)
    matrix.append([])
print(matrix)
########
def get_matrix(n):
    matrix = []
    for i in range(n):
        #print(i)
        matrix.append([])
    print(matrix)
result1 = get_matrix(3) # сколько передадим в функцию - столько выведет список
print(result1)
########
def get_matrix(n, m):
    matrix1 = []
    for i in range(n):
        matrix2 = []
        for j in range(m):
            #print(i)
            matrix2.append([]) # пустой
        matrix1.append(matrix2)
    print(matrix1)
result1 = get_matrix(3,2) # передадим напрмер 3 по 2 пустых
print(result1)
#################
#################  конечное программа
def get_matrix(n, m,value):
    matrix1 = []
    for i in range(n):
        matrix2 = []
        for j in range(m):
            #print(i)
            if value == 0: #если value = 0 то выводим пустой
                matrix2.append([])
            else:
                matrix2.append(value) #значение переменной
        matrix1.append(matrix2)
    print(matrix1)
result1 = get_matrix(2,2,10) #
result2 = get_matrix(3,5,42) #
result3 = get_matrix(4,2,13) #
result4 = get_matrix(3,2,0) #
print(result1)
print(result2)
print(result3)
print(result4)