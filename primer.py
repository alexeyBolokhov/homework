# Упражнение 1
# while True:
#     first = int(input("Введите 1-е число: "))
#     second = int(input("Введите 2-е число: "))
#     sum_ = print(f'сумма чисел: {first} + {second} =',first + second)
#     klava = str(input('Если закончиnь но нажмите y '))
#     if (klava == "Y" or klava == "y"):  break
# Упражнение 2

# print('------------------------------')
#
# n = 7
# print(n)
# for i in range(0,n):
#     for j in range(0,n):
#         if (i == 0 or i == n-1 or j==i or j == n-i-1):
#             print('X', end="")
#             #print(i)
#         else:
#             print(' ', end="")
#     print()
#Упражнение 3
# n=5
# k=1
# counter=1
# for i in range(n):
#     for j in range(n):
#         if k % 2 == 0:
#             print(counter, end ="  ")
#             counter+=1
#         else: print("*",end ="  ")
#         k+=1
#     print()

#Упражнение 4
h = 7
w = h + 2
m = w //4
for i in range(1, h+1):
    if (i <= m):
        print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
    else:
      print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))