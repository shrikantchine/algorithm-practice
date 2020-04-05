def bit_diff(A, B):
    X = A ^ B
    counter = 0
    while X != 0:
        X = X & (X-1)
        counter += 1
    return counter

print(bit_diff(10, 20))