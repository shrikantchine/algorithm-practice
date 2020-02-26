class Stack(object):
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        if self.empty():
            self.stack.append(val)
            self.min = val
        else:
            if val >= self.min:
                self.stack.append(val)
            else:
                self.stack.append(2*val-self.min)
                self.min = val

    def pop(self):
        val = self.stack.pop()
        if val >= self.min:
            return val
        else: 
            min_val_holder = self.min
            self.min = 2*self.min - val
            return min_val_holder

    def empty(self):
        return len(self.stack) == 0

    def get_min(self):
        return self.min


s = Stack()
s.push(3)
s.push(5)
print(s.get_min())
s.push(2)
s.push(1)
print(s.get_min())
print(s.pop())
print(s.get_min())
print(s.pop())