def count_binary(N):
    if N == 1:
        return 2
    ending_with_zero, ending_with_one = 1, 1
    x = 2
    while x <= N:
        tmp = ending_with_zero
        ending_with_zero = ending_with_one + ending_with_zero
        ending_with_one = tmp
        x += 1
    print(ending_with_zero + ending_with_one)

count_binary(3)