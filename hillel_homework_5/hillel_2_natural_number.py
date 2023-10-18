number = input("Введіть натуральне число: ")
if not number:
    exit()
number = int(number)
for num in range(1, number):
    square = num**2
    mod = 10**len(str(num))
    if square % mod == num:
        print(f"{num} * {num} = {square}")
    else:
        continue
