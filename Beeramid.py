def beeramid(bonus, price):
    print("New Test")

    if price == 0:
        return 1
    else:
        upper_bound = int(bonus // price)
    cum_total = 0
    levels = 0

    for i in range(1, upper_bound + 1):
        cum_total += i ** 2
        print(i ** 2, "iteration " + str(i))
        if cum_total <= upper_bound:
            levels += 1
        else:
            break
    return levels

if __name__ == "__main__":

    print(beeramid(1500, 2))
    print(beeramid(5000, 3))
    print(beeramid(-1, 4))
    print(beeramid(0, 4))
    print(beeramid(4, 0))