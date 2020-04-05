def count_frequencies(arr):
    max_val = max(arr)
    result = [0] * (max_val+1)
    for i in arr:
        result[i] += 1

    print(result[1:])

arr = [2, 3, 3, 2, 5]
count_frequencies(arr)