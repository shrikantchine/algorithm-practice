def group_reverse(arr, k):
    n = len(arr)
    i = 0
    while i < n:
        g = min(n-i, k)
        reverse(arr, i, g)
        i += g
    print(arr)


def reverse(arr, begin_index, n) :
    for i in range(n//2):
        arr[begin_index + i], arr[begin_index+ n-i-1] = arr[begin_index+n-i-1], arr[begin_index+i]

group_reverse([1, 2, 3, 4, 5], 3)