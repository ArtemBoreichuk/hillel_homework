import random


def generate(rows=3, columns=3):
    two_dimensional_list = []
    for _ in range(rows):
        row = [random.randint(0, 200) for _ in range(columns)]
        two_dimensional_list.append(row)
    return two_dimensional_list


def print_symmetric_table(two_dimensional_list):
    columns = len(two_dimensional_list[0])
    for row in two_dimensional_list:
        if len(row) != columns:
            print("Список не є симетричним.")
            return
    for row in two_dimensional_list:
        for value in row:
            print(f'{value:4}', end=' ')
        print()


table1 = generate()
print("Таблиця 1 (без параметрів):")
print_symmetric_table(table1)

table2 = generate(4)
print("\nТаблиця 2 (1 параметр - кількість рядків):")
print_symmetric_table(table2)

table3 = generate(4, 4)
print("\nТаблиця 3 (2 параметри - кількість рядків і стовпців):")
print_symmetric_table(table3)
