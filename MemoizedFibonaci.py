
# collaborator: peter.

dict_1 = {}

def fibonacci(n):
    if n in dict_1:
        return dict_1[n]
    if n in [1, 2]:
        a = 1
    else:
        a = fibonacci(n - 1) + fibonacci(n - 2)
    dict_1[n] = a
    return a

print(fibonacci(35))