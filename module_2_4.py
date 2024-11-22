# Задача "Всё не так уж просто":
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # содержащий только простые числа
not_primes = [] # содержащий все не простые числа
#j = 0
for i in numbers:
    if i == 1: #1 не является ни простым, ни составным
        continue  #в низ не пойдем
    is_prime = True  # флаг - простое
    for j in range(2, i): # делитель со 2го до

        if  i % j == 0: #   делится
            is_prime = False #
            break
    if is_prime: #
        #primes.append(i)
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)


