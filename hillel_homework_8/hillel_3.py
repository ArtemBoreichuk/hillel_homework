lst = [1, "1", {"1": 1}]
result_set = set()
for item in lst:
    try:
        result_set.add(item)
    except TypeError:
        continue
print(result_set)
