import random
matrix_n = int(input("Укажіть розмір квадратної матриці n: "))
matrix = [[random.randint(10, 99) for _ in range(matrix_n)] for _ in range(matrix_n)]
print("Матриця:")
for i in matrix:
    print(i)
x = sum(matrix[i][i] for i in range(matrix_n))
print(f"Сума чисел по діагоналі: {x}")
y = sum(row[-1] for row in matrix)
print(f"Сума чисел останнього стовбця: {y}")
