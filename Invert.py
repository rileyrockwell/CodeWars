def invert(lst):
    a = []
    for i in lst:
        a.append(i * (-1))

    return a

print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, 3, -4, 5]))
print(invert([]))
