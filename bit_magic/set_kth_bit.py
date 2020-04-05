def set_kth_bit(N, k):
    return (N | (N ^ (1 << k)))

print(set_kth_bit(10, 2))
print(set_kth_bit(15, 3))