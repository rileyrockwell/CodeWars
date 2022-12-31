# Collaborators: Peter Domitrovich
import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def is_prime(n):
    b = True
    for i in range(2, n):
        if n % i == 0:
            b = False
            break
    return b
def prime_list(n):
    # generate a list of all the primes of n
    # by the "sqrt prime factorization theorem"
    a = int(n**(1/2))
    b = []
    for i in range(2, a + 1):
        if is_prime(i) is True:
            b.append(i)
    return b

def decomp(n):
    x = factorial(n)

    # Alan: forget about calculating n!; focus on the factors of n!
    # evaluate 'decomp' on individual factors of n!; 'merge' the respective results to determine
    # the aggregate result.

    # find the prime factorization for x
    a = []
    y = x
    for i in prime_list(x):
        # by the "sqrt prime factorization theorem"
        if i > int(x**(1/2)):
            return a
        count = 0
        while y > 0:
            if y % i == 0:
                count += 1
                y = y // i
            else:
                break

        if count > 0:
            a.append(str(i) + "^" + str(count))

    return a

if __name__ == "__main__":
    print(factorial(5))