hypotenuse = lambda x, y=1: (x**2 + y**2)**0.5
num_1 = [3, 4, 5, 6]
result = list(map(lambda x: hypotenuse(x), num_1))
print("Результат одного списку:", result)
num_2_x = [1, 2, 3, 4]
num_2_y = [2, 3, 4, 5]
result_2 = list(map(lambda x, y: hypotenuse(x, y), num_2_x, num_2_y))
print("Результат двох списків:", result_2)
