'''
Boyer moore voting algorithm
'''

def majority_elem(arr):
    count = 0
    candidate = -1

    for i in arr:
        if count == 0:
            candidate = i
            count += 1
        else:
            if candidate == i:
                count += 1
            else:
                count -= 1

    print(candidate)
    return count

arr = [4, 7, 4, 4, 7, 4, 4, 9, 4, 3]
print(majority_elem(arr))