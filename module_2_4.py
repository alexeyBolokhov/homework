# Задача "Всё не так уж просто":
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # содержащий только простые числа
not_primes = [] # содержащий все не простые числа
#j = 0
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):

        if  i % j == 0: #  не делится на 2? без остатка
            is_prime = False
            break
    if is_prime:
        #primes.append(i)
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)

    # else:
    #     not_primes = numbers[j]
    #     print(not_primes)

# print(primes)
# print(not_primes)
# print(range(len(numbers)))