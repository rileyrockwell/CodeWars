def move_zeros(array):
    for int in array:
        if int == 0:
            array.pop(int)
            array.append(int)
    return array