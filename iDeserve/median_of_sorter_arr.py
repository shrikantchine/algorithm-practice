def median_of_arr(arr1, arr2, n):
    if n == 0:
        return -1
    if n == 1:
        return (arr1[0]+arr2[0])/2
    if n ==2:
        return (max(arr1) + min(arr2))/2
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)
        if m1 > m2:
            if n%2 == 0:
                return median_of_arr(arr1[:(n//2)+1], arr2[(n//2)-1:], n//2+1)
            else:
                return median_of_arr(arr1[(n//2)-1:], arr2[:(n//2)+1], n//2+1)
        else:
            if n%2 == 0:
                return median_of_arr(arr2[:(n//2)+1], arr1[(n//2)-1:], n//2+1)
            else:
                return median_of_arr(arr2[(n//2)-1:], arr1[:(n//2)+1], n//2+1)



def median(arr, n):
    if n%2 != 0:
        return arr[n//2]
    else:
        return (arr[n//2] + arr[(n//2)]-1)/2


# Driver code 
arr1 = [1, 2, 3, 6] 
arr2 = [4, 6, 8, 10] 
n = len(arr1) 
print(int(median_of_arr(arr1,arr2,n))) 