x = "Python is good language to learn and in same time we like to tell that it is cool experience for us"
y = {}
for q in x:
    if q.isalpha():
        if q in y:
            y[q] += 1
        else:
            y[q] = 1
print(y)
