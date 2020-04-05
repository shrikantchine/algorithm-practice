def right_rotate(n, d, INT_BITS=16):
    return (n >> d) | (n << (INT_BITS-d)) & 0xFFFF

def left_rotate(n, d, INT_BITS=16):
    return (n << d) | (n >> (INT_BITS-d))


print(right_rotate(28, 2))
print(left_rotate(28, 2))