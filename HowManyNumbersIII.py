def find_all(sum_dig, digs):
    '''
    implement a function which receives two arguments:
    1. the sum of digits (sum)
    2. the number of digits (count)

    return 3 values:
    1. the total number of values which have 'count' digits
    that add up to 'sum' and are in increasing order
    2. the lowest such value
    3. the greatest such value

    Note: if there are no value which satisfy these constraints,
    you should return an empty value (refer to the examples to
    see what exactly is expected).
    '''

    a = [int(i) for i in str(sum_dig)]
    sum = 0
    for i in a:
        sum += i


    # return 3 values:
    # 1. total number of values which have 'count' digits that add up to 'sum' and are in increasing order
    # 2. the lowest such value
    # 3. the greatest such value

    return a, sum

if __name__ == "__main__":
    sum_dig = 131
    dig = 3
    print(find_all(sum_dig, dig))