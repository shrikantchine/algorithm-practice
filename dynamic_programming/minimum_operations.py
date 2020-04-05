'''
You are given a number N. You have to find the number of operations required to reach N from 0. You have 2 operations available:

Double the number
Add one to the number
'''


def min_operations(N):
    min_op_holder = [0] * (N+1)
    for i in range(1, N+1):
        if i%2 == 0:
            min_op_holder[i] = min_op_holder[i//2] + 1
        else: 
            min_op_holder[i] = min_op_holder[i-1] + 1
    print(min_op_holder)
    return min_op_holder[-1]

    
print(min_operations(15))