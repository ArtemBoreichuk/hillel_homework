def inp_sum():
    try:
        value_1 = input("Введіть перше значення: ")
        value_2 = input("Введіть друге значення: ")
        num_1 = float(value_1)
        num_2 = float(value_2)
        result = num_1 + num_2
    except ValueError:
        result = str(value_1) + str(value_2)
    return result


result = inp_sum()
print("Результат:", result)
