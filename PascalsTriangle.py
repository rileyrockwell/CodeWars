def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def pascals_triangle(n):
    a = []
    # loop for the row
    for i in range(1,n+1):
        # loop for the column
        for k in range(i):
            a.append(binomial_coefficient(i-1, k))
    return a


if __name__ == "__main__":
    print(pascals_triangle(1))
    print(pascals_triangle(2))
    print(pascals_triangle(4))