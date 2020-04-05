def find_odd_number(arr):
    X = 0
    for i in arr:
        X = X ^ i
    print(X)

find_odd_number([2, 2, 4, 4, 4, 5, 5])