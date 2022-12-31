def doubles(maxk, maxn):
    cumulative_sum = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            cumulative_sum += 1 / (k*(n + 1)**(2*k))

    return cumulative_sum

if __name__ == "__main__":
    print(doubles(1, 3))
    print(doubles(1, 10))
    print(doubles(10, 100))