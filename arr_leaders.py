"""
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader. 
"""

def leaders(arr):
    max_val = arr[-1]
    result = []
    for i in reversed(list(range(len(arr)))):
        if arr[i] >= max_val:
            result.append(arr[i])
            max_val = arr[i]

    return result

print(leaders([16,17,4,3,5,2]))
print(leaders([7,4,5,7,3]))