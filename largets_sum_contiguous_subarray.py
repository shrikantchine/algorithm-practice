def largest_sum(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in arr:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

print(largest_sum([-2, -3, 4, -1, -2, 1, 5, -3]))