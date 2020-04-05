def isset(N, k):
    if k == 0:
        return (N & 1) == 1
    else:
        return (N >> k) == 1

print(isset(4, 0))
print(isset(4, 2))