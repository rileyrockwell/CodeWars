# Collaborators: Peter Domitrovich
def interlockable(a, b):
    # ensure both a and b are positive
    if (a or b) < 0:
        print("Please enter positive integer input.")
        return False

    # generate the binary representation of 'a' and 'b'.
    a = bin(a)
    b = bin(b)

    a = a[2:]
    b = b[2:]

    c = len(a) - 1
    d = len(b) - 1

    for i in range(min(len(a), len(b))):
        if a[c] == b[d] and a[c] == "1":
            return False
        c -= 1
        d -= 1

    return True

print(interlockable(3, 6))