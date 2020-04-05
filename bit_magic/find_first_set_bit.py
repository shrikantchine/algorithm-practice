def find_first_set_bit(n):
    counter = 1
    while n & 1 != 1:
        counter += 1
        n = n >> 1
    return counter

print(find_first_set_bit(18))