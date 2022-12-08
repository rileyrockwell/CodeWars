def expanded_form(num):
    a = num
    b = [int(i) for i in str(a)]
    c = []

    for i in range(len(b)):
        c.append(b[-(i+1)] * 10**i)

    c.reverse()

    d = []
    for i in c:
        if i != 0:
            d.append(i)

    e = [str(i) for i in d]

    f = " + ".join(e)

    return f

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))