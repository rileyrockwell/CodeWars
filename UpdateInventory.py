cur_stock = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]

def update_inventory(cur_stock, new_stock):
    updated_stock = []
    for i in cur_stock:
        a = i[1]
        print(a, " * ")
        updated_stock.append(i)
        for k in new_stock:
            if k[1] == a:
                updated_stock.append(i[0] + k[0])

    return updated_stock

print(update_inventory(cur_stock, new_stock))