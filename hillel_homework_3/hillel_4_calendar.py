year = int(input("Введіть рік: "))
if year < 1900 or year > 1_000_000:
    print("Рік не відповідає умовам.")
else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "є високосним роком")
            else:
                print(year, "не є високосним роком")
        else:
            print(year, "є високосним роком")
    else:
        print(year, "не є високосним роком")

print('-' * 30)

year = int(input("Введіть рік: "))
if 1900 < year < 1_000_000:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "є високосним роком")
            else:
                print(year, "не є високосним роком")
        else:
            print(year, "є високосним роком")
    else:
        print(year, "не є високосним роком")
else:
    print("Рік не відповідає умовам.")