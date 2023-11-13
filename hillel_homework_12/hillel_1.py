import random


def generate_and_sort_matrix(M):
    matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]
    column_sums = [sum(column) for column in zip(*matrix)]
    sorted_indexes = [index for (sum_, index) in sorted(zip(column_sums, range(M)))]
    matrix = [[row[i] for i in sorted_indexes] for row in matrix]
    for index in range(M):
        if index % 2 == 0:
            matrix = [list(row) for row in zip(*[sorted(column) if i == index else column for i, column in enumerate(zip(*matrix))])]
        else:
            matrix = [list(row) for row in zip(*[sorted(column, reverse=True) if i == index else column for i, column in enumerate(zip(*matrix))])]
    return matrix


def print_matrix(matrix):
    M = len(matrix)
    for row in matrix:
        print(" ".join(f"{num:2d}" for num in row))
    column_sums = [sum(column) for column in zip(*matrix)]
    print(" ".join(f"{sum_:2d}" for sum_ in column_sums))


M = 6
matrix = generate_and_sort_matrix(M)
print_matrix(matrix)
