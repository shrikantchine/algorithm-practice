def rightmost_diff(a, b):
    c = a ^ b
    counter = 1
    while c & 1 != 1:
        c = c >> 1
        counter += 1

    return counter

print(rightmost_diff(11, 9))
print(rightmost_diff(52, 4))