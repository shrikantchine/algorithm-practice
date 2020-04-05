"""
You are given N pairs of numbers. In every pair, the first number is always smaller than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. Your task is to complete the function maxChainLen which returns an integer denoting the longest chain which can be formed from a given set of pairs. 
"""

# Does not work without sorting of pair
def max_len_chain(arr, index=0, result=[]):
    #print(result)
    if index > len(arr)-2:
        return 0
    if len(result) == 0 or result[-1] < arr[index]:
        # We can add the pair
        return max(max_len_chain(arr, index+2, arr[:index+2])+1, max_len_chain(arr, index+2, arr[:index+2]))
    #Otherwise we cannot add the pair
    return max_len_chain(arr, index+2, arr[index:index+2])


print(max_len_chain([1, 2, 5,24,39,60,15,28,27,40,50,90]))
print(max_len_chain([5,10,1,11]))