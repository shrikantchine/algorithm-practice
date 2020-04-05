def toggle_all_bits(n):
    y = n
    for i in range(len(bin(n))-2):
        y = y ^ (1 << i)

    print(y)


toggle_all_bits(50)