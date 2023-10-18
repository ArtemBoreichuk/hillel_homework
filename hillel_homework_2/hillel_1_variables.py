x = 1
y = 2
z = x
x = y
y = z
print(x, y)
print(y, x)

x = 1
y = 2
x, y = y, x
print(x, y)
print(y, x)

x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))
x = x + y
y = x - y
x = x - y
print("Значение x после замены:", x)
print("Значение y после замены:", y)
