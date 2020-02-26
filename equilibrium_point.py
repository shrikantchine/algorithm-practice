"""
Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array. Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
"""

def find_equilibrium(arr):
    before_sum = [-1] * len(arr)
    after_sum = [-1] * len(arr)

    before_sum[0] = 0
    for i in range(1, len(arr)):
        before_sum[i] = before_sum[i-1] + arr[i-1]

    after_sum[-1] = 0
    for i in reversed(list(range(0, len(arr)-1))):
        after_sum[i] = after_sum[i+1] + arr[i+1]

    count = 0
    for i, j in zip(before_sum, after_sum):
        if i == j:
            return count
        count += 1
    return -1


def efficient_find_equilibrium(arr):
    right_sum = sum(arr)
    left_sum = 0
    for i, val in enumerate(arr):
        right_sum -= val
        if left_sum == right_sum:
            return i
        left_sum += val
    return -1

print(find_equilibrium([1,3,5,2,2]))
print(efficient_find_equilibrium([1,3,5,2,2]))