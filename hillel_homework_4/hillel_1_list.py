x = input("Введіть рядок з 15 символів: ")
if len(x) == 0:
    print("Введіть значення з 15-ти сомволів у рядок.")
else:
    if len(x) < 15:
        x = x * 3
        print("Результат 15-ти символів:", x)
        y = list(x)
        print("Повний список:", y)
        print("Список в якому виведено останні 5 елементів:", y[-5:])
        print("Cписок (зеркально обернено) в зворотній послідовності:", y[::-1])
        print("Cписок усіх елементів з парними індексами:", y[::2])
        y[:5] = y[-5:]
        print("Cписок у якому 5 елементів спочатку такі ж самі як остані 5 елементів списку:", y)
