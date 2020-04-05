'''
Given an array of integers A and a sum B, find all unique combinations in A where the sum is equal to B.

ach number in A may only be used once in the combination.

Note:
   All numbers will be positive integers.
   Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
   The combinations themselves must be sorted in ascending order.
   If there is no combination possible the print "Empty" (without qoutes).
Example,
Given A = 10,1,2,7,6,1,5 and B(sum) 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

def combination_sum(arr, target, partial=[]):
    s = sum(partial)
    if s == target:
        print(partial)
    if s >= target:
        return
    for i in range(len(arr)):
        n = arr[i]
        remaining = arr[i+1:]
        combination_sum(remaining, target, partial+[n])

combination_sum([10,1,2,7,6,1,5], 8)