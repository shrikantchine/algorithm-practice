def next_larger_elem(arr):
    stack = [-1]

    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            stack.append(arr[i+1])
        else: 
            stack.append(stack[-1])
    stack.reverse()
    return stack

print(next_larger_elem([1, 3, 2, 4]))