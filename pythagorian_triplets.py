import math

def pythagorian_triplets(arr):
    maximum = max(arr)
    hash = [0] * (maximum+1)
    for val in arr:
        hash[val] += 1
    
    for i in range(maximum+1):
        if hash[i] == 0:
            continue
        for j in range(maximum+1):
            if (i == j and hash[i] == 1) or hash[j] == 0:
                continue
            val = int(math.sqrt(i*i + j*j))
            if val*val != (i*i + j*j):
                continue
            if val > maximum:
                continue
            if hash[val]:
                return True
    return False

print(pythagorian_triplets([3,2,4,6,5]))