"""
Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.
"""

def find_pairs(arr1, arr2, X):
    hash_map = {}
    result = []
    for i in arr1:
        hash_map[X-i] = i
    for i in arr2:
        if i in hash_map:
            result.append((i, hash_map[i]))
    return result

print(find_pairs([1, 2, 4, 5, 7], [5, 6, 3, 4, 8], 9))