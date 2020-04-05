def zero_sum_subarr(arr):
    hash_map = {}
    curr_sum = 0
    result = []
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            result.append((0, i))
        x = []
        if curr_sum in hash_map:
            x = hash_map[curr_sum]
            for j in x:
                result.append((j+1, i))
        x.append(i)
        hash_map[curr_sum] = x
    return result


arr = [0,0,5, 5, 0, 0]
print(zero_sum_subarr(arr))