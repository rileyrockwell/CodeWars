def multiplication_table(size):
    parent_array = []
    for i in range(1, size+1):
        child_array = []
        for k in range(1, size+1):
            child_array.append(i*k)
        parent_array.append(child_array)
    return parent_array

if __name__ == "__main__":
    print(multiplication_table(3))