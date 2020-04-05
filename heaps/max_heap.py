class MaxHeap(object):
    def __init__(self):
        self.heap = ['N']
        self.size=0

    def empty(self):
        return self.size < 1
    
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.swim(self.size)

    def swim(self, k):
        while k > 1 and self.heap[k] > self.heap[k//2]:
            self.heap[k//2], self.heap[k] = self.heap[k], self.heap[k//2]
            k = k//2
    
    def delete_max(self):
        if self.empty():
            return
        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        max_val = self.heap.pop()
        self.size -= 1
        self.sink(1)
        return max_val

    def sink(self, k):
        while (2*k) <= self.size:
            j = 2*k
            if j < self.size and self.heap[j] < self.heap[j+1]:
                j += 1
            if self.heap[k] < self.heap[j]:
                self.heap[j], self.heap[k]= self.heap[k], self.heap[j]
            k = j

    def __str__(self):
        return str(self.heap[1:])



H = [21, 1, 45, 78, 3, 5]
heap = MaxHeap()
for i in H:
    heap.insert(i)  
print(str(heap))
heap.delete_max()
print(str(heap))
print(H)