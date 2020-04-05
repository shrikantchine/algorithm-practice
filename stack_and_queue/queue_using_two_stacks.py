def qPush(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    stack1.append(x)
    
    #code here

def qPop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    if len(stack2) == 0 and len(stack1) == 0:
        return -1
    if len(stack2) == 0:
        while len(stack1) > 0:
            stack2.append(stack1.pop())

    return stack2.pop()    
    #code here