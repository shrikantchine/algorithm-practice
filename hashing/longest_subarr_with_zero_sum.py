'''
Given an array having both positive an negative integers. The task is to complete the function maxLen() which returns the length of maximum subarray with 0 sum. The function takes two arguments an array A and n where n is the size of the array A.
'''
from collections import defaultdict

def longest_subarr_with_zero_sum(arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if arr[i] == 0 and max_len == 0:
            max_len = 1
        if curr_sum == 0:
            max_len = i+1
        if curr_sum in hash_map:
            max_len = max(max_len, i-hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i

    return max_len
        
arr = [15, -2, 2, -8, 1, 7, 10, 13] 
   
print(longest_subarr_with_zero_sum(arr))