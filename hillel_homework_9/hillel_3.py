import random
numbers = set(random.sample(range(1, 101), 15))
x = {i for i in numbers if i % 2 == 0}
y = {i for i in numbers if i % 2 != 0}
x1 = sum(x)
y1 = sum(y)
if x1 > y1:
    print("Так")
else:
    print("Ні")

# print("-" * 75)
# print("Множина чисел:", numbers)
# print("Сума парних чисел:", x1)
# print("Сума непарних чисел:", y1)
