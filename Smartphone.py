def update_inventory(cur_stock, new_stock):
    unique_cur_stock = []
    unique_new_stock = []
    unique_matches = []

    # parent: cur_stock
    # child: new_stock
    for i in cur_stock:
        binary_array = []
        for j in new_stock:
            # condition 1: no match
            if i[1] != j[1]:
                binary_array.append(0)
            # condition 2: match
            elif i[1] == j[1]:
                binary_array.append(1)

        print(binary_array)

        if sum(binary_array) == 0:
            unique_cur_stock.append(i)

    print(unique_cur_stock)

    # parent: new_stock
    # child: cur_stock
    for i in new_stock:
        binary_array = []
        for j in cur_stock:
            # condition 1: no match
            if i[1] != j[1]:
                binary_array.append(0)
            # condition 2: match; redundant
            elif i[1] == j[1]:
                binary_array.append(1)

        print(binary_array)

        if sum(binary_array) == 0:
            unique_new_stock.append(i)

    print(unique_new_stock)

    # parent: cur_stock
    # child: new_stock
    for i in cur_stock:
        binary_array = []
        for j in new_stock:
            # condition 1: no match
            if i[1] != j[1]:
                binary_array.append(0)
            # condition 2: match
            elif i[1] == j[1]:
                binary_array.append(1)
                cum_total = i[0] + j[0]

        print(binary_array)

        if sum(binary_array) == 1:
            element = cum_total, i[1]
            unique_matches.append(element)

    print(unique_matches)

    # combine all 3 lists, and sort alphabetically
    updated_list = unique_cur_stock + unique_new_stock + unique_matches
    updated_list_sorted = sorted(updated_list, key=lambda x: x[1])

    return updated_list_sorted

if __name__ == "__main__":
    cur_stock = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
    new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]
    print(update_inventory(cur_stock, new_stock))

# references
# https://learnpython.com/blog/sort-alphabetically-in-python/

