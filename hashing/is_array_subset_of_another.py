from collections import defaultdict

def is_subset(arr1, arr2):
    hash_map = defaultdict(int)
    for i in arr2:
        hash_map[i] += 1

    for i in arr1:
        hash_map[i] -= 1
    
    for _, val in hash_map.items():
        if val != 0 and val != -1:
            return False
    return True

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

print(is_subset(arr1, arr2))

arr1 = [10, 5, 2, 23, 19]
arr2 = [19, 5, 3]

print(is_subset(arr1, arr2))