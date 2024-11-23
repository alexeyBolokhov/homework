#Задание "Слишком древний шифр":
def rebus(n):
    stroka = ''
    sum_ = 0
    # print(list_1)
    for i in range(1, n):  # 5
        for j in range(1 + i, n): # 1 + i чтобы не было 14 и 41 23 и 32
            sum_ = (i + j)
            if n % sum_ == 0:  # 1 + 4, 2 + 3 # 5
                #print(i, j)
                # print(n)
                stroka = stroka + str(i) + str(j)
    return stroka

n = int(input("Введите число от 3 до 20: "))
print('Вы ввели число: ',n)
if n < 3 or n > 20:
    print('Вы ввели число вне диапозона: ')
else:
    #rebus(n)
    print(rebus(n))
######################
    # stroka = ''
    # sum_ = 0
    # #print(list_1)
    # for i in range(1,n): #5
    #     for j in range(1+i,n):
    #         sum_ = (i + j)
    #         if  n % sum_ == 0:   #1 + 4, 2 + 3 # 5
    #             print(i,j)
    #             #print(n)
    #             stroka = stroka+ str(i)+str(j)
    #             #print(sum_)
    #             #print(n % sum_)






        #list_1.append(list_2)
# nums = [12,23,34,45,56,67,78,89,12,23,45,78]
# alt_nums = []
# for num in nums:

#     #num += 10
#     alt_nums.append(num)
#print(alt_nums)


