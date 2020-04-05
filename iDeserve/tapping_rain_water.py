def water_tapping(arr):
    left_max = [0] * (len(arr))
    right_max = [0] * (len(arr))
    for i in range(1, len(arr)):
        left_max[i] = max(arr[i-1], left_max[i-1])
    
    for i in range(len(arr)-2, -1, -1):
        right_max[i] = max(arr[i+1], right_max[i+1])

    quantity = 0
    for i, val in enumerate(arr):
        q = (min(left_max[i], right_max[i]) - val)
        if q > 0:
            quantity += q

    print(quantity)



water_tapping([1, 5, 2, 3, 1, 7, 2, 4])