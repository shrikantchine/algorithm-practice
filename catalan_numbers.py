"""
Recursive formula
c[0] = 1 and c[n=1] = sum_from_zero_to_n(c[i][n-1]) for n >= 0
"""

def catalan(n, cache=None):
    if n <= 1:
        return 1
    result = 0
    if not cache:
        cache = [-1] * n
    for i in range(n):
        if cache[i] == -1:
            cache[i] = catalan(i)
        if cache[n-i-1] == -1:
            cache[n-i-1] = catalan(n-i-1)
        result += cache[i]*cache[n-i-1]
    return result

print(catalan(20))