numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        not_primes.append(i)
        not_primes.remove(1)
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('Not_primes: ', not_primes)