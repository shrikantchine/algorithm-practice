"""
Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2, append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.
"""

from collections import defaultdict

def relative_sorting(A1, A2):
    store = defaultdict(lambda: -1)
    result = []
    remaining = []
    for i in A2:
        store[i] = 0
    for i in A1:
        if store[i] >= 0:
            store[i] += 1
    
    for i in A2:
        if store[i] != -1:
            result.extend([i] * store[i])
            store[i] = 0

    for i in A1:
        if store[i] == -1:
            remaining.append(i)

    remaining.sort()
    result.extend(remaining)
    return result


print(relative_sorting([2,  1,  2,  5,  7,  1,  9,  3,  6,  8,  8], [2, 1, 8, 3]))
    