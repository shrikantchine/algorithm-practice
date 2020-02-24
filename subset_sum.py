def subset_sum(s, k):
    if k == 0:
        return []
    if len(s) == 0:
        return None
    r1 = subset_sum(s[1:], k)
    r2 = subset_sum(s[1:], k-s[0])
    if r1 is not None:
        return r1
    if r2 is not None:
        return r2 + [s[0]]


S = [12, 1, 61, 5, 9, 2]
K = 24
print(subset_sum(S, K))