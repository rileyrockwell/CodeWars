# referencing: https://bobbyhadz.com/blog/python-split-integer-into-digits

def last_digit(n1, n2):
    a = [int(i) for i in str(n1)][-1]
    b = n2

    c = [int(i) for i in str(a**b)]

    d = c[-1]

    print(a)
    print(b)
    print(c)
    print(d)

# cyclicity:
a2 = [2, 4, 6, 8]
a3 = [3, 9, 7, 1]

print(last_digit(2**100,2**200))