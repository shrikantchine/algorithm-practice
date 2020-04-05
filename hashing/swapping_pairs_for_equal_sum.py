"""
Given two arrays of integers, write a program to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.
"""

def swapping(A, B):
    sum_A = sum(A)
    sum_B = sum(B)

    hash_map = {}

    for i in B:
        hash_map[i+sum_A] = i
    for i in A:
        if (sum_B-i) in hash_map:
            return i, hash_map[sum_B-i]

    return -1

A = [4, 1, 2, 1, 1, 2]
B = [3, 6, 3, 1]

print(swapping(A, B))