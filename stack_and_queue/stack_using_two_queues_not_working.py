#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
def push_in_stack(x):
    
    # global declaration
    global queue_1
    global queue_2
    if len(queue_1) != 0:
        queue_1.append(x)
    elif len(queue_2) != 0:
        queue_2.append(x)
    else:
        queue_1.append(x)
    # code here
    
def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    if len(queue_1) == 0 and len(queue_2) == 0:
        return -1
    if len(queue_1) != 0:
        while len(queue_1) > 1:
            queue_2.append(queue_1.pop(0))
        return queue_1.pop()
    while (len(queue_2)) > 0:
        queue_1.append(queue_2.pop(0))
    return queue_2.pop()
    
    # code here

#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
def push_in_stack(x):
    
    # global declaration
    global queue_1
    global queue_2
    if len(queue_1) != 0:
        queue_1.append(x)
    elif len(queue_2) != 0:
        queue_2.append(x)
    else:
        queue_1.append(x)
    # code here
    
def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    if len(queue_1) == 0 and len(queue_2) == 0:
        return -1
    if len(queue_1) != 0:
        while len(queue_1) > 1:
            queue_2.append(queue_1.pop(0))
        return queue_1.pop()
    while (len(queue_2)) > 1:
        queue_1.append(queue_2.pop(0))
    return queue_2.pop()
    
    # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha
queue_1 = [] # first queue
queue_2 = [] # second queue

if __name__ == '__main__':
    push_in_stack(10)
    push_in_stack(20)
    print(pop_from_stack())
    print(pop_from_stack())
# } Driver Code Ends