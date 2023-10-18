numbers = input("Введіть число: ")
if not numbers:
    exit()
print(numbers)
numbers = list(numbers)
for number in numbers:
    numbers_ = numbers
    numbers_.remove(number)
    if number in numbers:
        print("Так")
        exit()
else:
    print("Ні")
    exit()
