def beeramid(bonus, price):
    upper_bound = int(bonus // price)
    cum_total = 0
    levels = 0
    for i in range(1, upper_bound):
        cum_total += i**2
        levels += 1
        if cum_total >= upper_bound:
            break

    return levels - 1


if __name__ == "__main__":
    print(beeramid(1500, 2))
    print(beeramid(5000, 3))
    print(beeramid(1500, 3))