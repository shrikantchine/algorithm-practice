def toggle(N, L, R):
    for i in range(L, R+1):
        N = N ^ (1 << (i-1))
    return N

print(toggle(17, 2, 3))