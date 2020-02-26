"""
Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.
"""

def rearrange(arr):
    max_index = len(arr)-1
    min_index = 0
    max_elem = arr[max_index] + 1

    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] += (arr[max_index] % max_elem) * max_elem
            max_index -= 1
        else:
            arr[i] += (arr[min_index] % max_elem) * max_elem
            min_index += 1

    for i in range(len(arr)):
        arr[i] //= max_elem


arr = [1, 2, 3, 5, 6, 7]
rearrange(arr)
print(arr)
    