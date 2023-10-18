numbers = []
even = 0
odd = 0
while True:
    num = input("Введіть число (0 для завершення): ")
    num = int(num)
    if num == 0:
        break
    if num % 2:
        odd += 1
    else:
        even += 1
    numbers.append(num)
print("Сумма чисел:", sum(numbers))
print("Середнє арифметичне:", sum(numbers)/len(numbers))
print("Мінімальне:", min(numbers), "\n" "Максимальне:",  max(numbers))
print("Парні:", even, "\n" "Непарні:", odd)
