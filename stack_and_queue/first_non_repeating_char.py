def first_non_repeating_char(arr):
    count_arr = [0] * 26

    queue = []
    result = []

    for i in arr:
        index = ord(i) - ord('a')
        if len(queue) == 0:
            queue.append(i)
            count_arr[index] += 1
            result.append(i)
        else:
            if count_arr[index] == 0:
                count_arr[index] += 1
                result.append(queue[0])
                queue.append(i)
            else: 
                count_arr[index] = 1
                queue.pop(0)
                result.append(queue[0] if len(queue) > 0 else -1)
    return result

print(first_non_repeating_char(['a', 'a', 'b', 'c']))