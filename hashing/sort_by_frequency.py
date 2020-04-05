"""
Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.
"""
from collections import defaultdict
import operator

def frequency_sort(arr):
    freq_store = defaultdict(int)
    same_freq_store = defaultdict(list)
    result = []
    for i in arr:
        freq_store[i] += 1
    for i, val in freq_store.items():
        same_freq_store[val].append(i) 
    
    for i, val in same_freq_store.items():
        val = sorted(val)
        for j in val:
            result.extend([j] * i)

    return result

print(frequency_sort([5, 5, 4, 6, 4]))
print(frequency_sort([9, 9, 9, 2, 5]))