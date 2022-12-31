def prime(n):
    # assume n is prime
    a = []
    for i in range(2, n + 1):
        # if n is composite
        if n % i == 0:
            break
        # if n is prime, append n to the list
        else:
            a.append(i)
    return a


if __name__ == "__main__":
    print(prime(7))
    print(prime(8))