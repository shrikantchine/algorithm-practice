"""
Given three increasingly sorted arrays A, B, C of sizes N1, N2, and N3 respectively, you need to print all common elements in these arrays.

Note: Please avoid printing the same common element more than once.
"""

from collections import defaultdict

def common_element(A, B, C):
    hash_A = defaultdict(int)
    hash_B = defaultdict(int)
    result = set()
    for i in A:
        hash_A[i] = 1
    for i in B:
        hash_B[i] = 1
    for i in C:
        if hash_A[i] == 1 and hash_B[i] == 1:
            result.add(i)
    return result

A =[1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(common_element(A, B, C))