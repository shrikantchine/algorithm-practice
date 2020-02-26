"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.
"""
def ugly_numbers(n):
    if n == 0:
        return None
    if n == 1:
        return 1
    ugly = [1]
    i2, i3, i5 = 0,0,0
    next_multiple_2, next_multiple_3, next_multiple_5 = 2, 3, 5
    for _ in range(n-1):
        ugly.append(min(next_multiple_2, next_multiple_3, next_multiple_5))
        if ugly[-1] == next_multiple_2:
            i2 += 1
            next_multiple_2 = ugly[i2]*2
        if ugly[-1] == next_multiple_3:
            i3 += 1
            next_multiple_3 = ugly[i3]*3
        if ugly[-1] == next_multiple_5:
            i5 += 1
            next_multiple_5 = ugly[i5]*5
    return ugly[-1]
        

assert ugly_numbers(7) == 8
assert ugly_numbers(10) == 12
assert ugly_numbers(15) == 24
assert ugly_numbers(150) == 5832