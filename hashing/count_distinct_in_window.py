"""
Given an array A[] of size N and an integer K. Your task is to complete the function countDistinct() which prints the count of distinct numbers in all windows of size k in the array A[].
"""

from collections import defaultdict

def count_distinct(A, k):
    hash_map = defaultdict(int)
    result = []
    for i in range(len(A)):
        if i < k:
            hash_map[A[i]] += 1
        else:
            index = i-k
            hash_map[A[index]] -= 1
            hash_map[A[i]] += 1
        if i >= k-1:
            result.append(len([x for x in hash_map if hash_map[x] > 0]))
    return result

print(count_distinct([1, 2, 1, 3, 4, 2, 3], 4))