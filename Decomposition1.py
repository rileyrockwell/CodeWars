# Collaborators: Peter Domitrovich
import time


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(n):
    b = True
    for index in range(2, n):
        if n % index == 0:
            b = False
            break
    return b


def prime_list(n):
    # generate a list of all the primes of n
    a = []
    for i in range(2, n + 1):
        if is_prime(i) is True:
            if n % i == 0:
                a.append(i)
    return a


def decomposition(n):
    x = factorial(n)

    # find the prime factorization for x
    a = []
    y = x
    for index in prime_list(x):
        count = 0
        while y > 0:
            if y % index == 0:
                count += 1
                y = y // index
            else:
                break

        if count > 0:
            a.append(str(index) + "^" + str(count))

    return a


if __name__ == "__main__":
    print(prime_list(factorial(7)))
    print(prime_list(factorial(8)))
    print(prime_list(factorial(9)))