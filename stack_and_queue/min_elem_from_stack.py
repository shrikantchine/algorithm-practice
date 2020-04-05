import sys

class Stack(object):
    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, x):
        if x > self.min:
            self.stack.append(x)
        else:
            self.min = x
            self.stack.append(2*x - self.min)
    
    def pop(self):
        x = self.stack.pop()
        if self.min > x:
            min_copy = self.min
            self.min = (2*self.min) - x
            return min_copy
        else:
            return x

    def getMin(self):
        return self.min

    def __str__(self):
        return str(self.stack)

s = Stack()
print(s.push(3))
print(s.push(5))
print(s.getMin())
print(s.push(2))
print(s.push(1))
print(s.getMin())
print(s.pop())
print(s.getMin())
print(s.pop())
print(s.pop())