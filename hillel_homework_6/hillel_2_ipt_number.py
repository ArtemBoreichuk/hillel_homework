n = int(input("Введіть число: "))
max_length = len(str(10**n)) + len(str(n))
for i in range(n):
    number = 10**i
    print(f"{i:>{len(str(n))}} {number:>{max_length - len(str(n))}}")
