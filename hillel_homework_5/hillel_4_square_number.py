N = int(input('Введіть число "N": '))
for i in range(1, N):
    x = i*i
    if x >= N:
        break
    print(x, end=" ")
