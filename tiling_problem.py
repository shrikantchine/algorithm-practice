def tiling(n, cache=None):
    if n == 1 or n == 2:
        return n
    if cache is None:
        cache = [-1] * n
    if cache[n-1] == -1:
        cache[n-1] = tiling(n-1)
    if cache[n-2] == -1:
        cache[n-2] = tiling(n-2)
    return cache[n-1] + cache[n-2]

assert tiling(3) == 3
assert tiling(2) == 2
assert tiling(1) == 1
assert tiling(4) == 5
assert tiling(5) == 8