def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(p, g):
    for number in range(p, g + 1):
        if is_prime(number):
            yield number


import random
n = random.randint(1, 50)
z = random.randint(51, 100)
result = list(prime_generator(n, z))
print(f"Прості числа у діапазоні від {n} до {z}: {result}")
