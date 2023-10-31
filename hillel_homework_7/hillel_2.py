import random
x = {f'key_{i}': random.randint(1, 10) for i in range(20)}
y = 1
for value in x.values():
    y *= value
print("Словник з випадковими числами:", x)
print("Результат множення чисел у словнику:", y)
