def max_of_subarr(arr, k):
    result = []

    result.append(max(arr[:k]))
    for i in range(k, len(arr), 1):
        if result[-1] > arr[i]:
            result.append(result[-1])
        else:
            result.append(arr[i])
    return result


print(max_of_subarr([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))