"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
"""

def subset_sum(arr, sum):
    if sum == 0:
        return True
    if len(arr) == 0:
        return False
    return subset_sum(arr[1:], sum-arr[0]) or subset_sum(arr[1:], sum)

arr = [3, 34, 4, 12, 5, 2]
sum = 9
print(subset_sum(arr, sum))