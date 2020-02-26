def find_missing_numer(arr):
    X1 = arr[0]
    X2 = 1
    for i in arr[1:]:
        X1 = X1 ^ i

    for i in range(2, len(arr)+2):
        X2 = X2 ^ i

    return X1 ^ X2

print(find_missing_numer([1, 2, 3, 5, 6]))