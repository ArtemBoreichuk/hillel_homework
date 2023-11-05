import random
int_elements = [random.randint(1, 500) for x in range(25)]
print(int_elements)
x1 = [x**2 for x in int_elements]
print(x1)
x2 = [x % 11 for x in int_elements]
print(x2)
x3 = [x for x in int_elements if x % 2 == 0]
print(x3)
x4 = [x for x in int_elements if len(str(x)) % 2 != 0]
print(x4)
x5 = [int_elements[i] for i in range(len(int_elements)) if i % 3 != 0]
print(x5)
