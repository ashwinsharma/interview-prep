"""
References:
    - https://www.youtube.com/watch?v=E2v9hBgG6gE
    - https://www.geeksforgeeks.org/min-heap-in-python/

This is a list based implementation of a min heap.
In a 0-indexed list, for an element at index i:
    - the parent node is at index (i-1)//2
    - the left child is at index (2*i)+1
    - the right child is at index (2*i)+2
where '//' is the floor division operator.
"""

import random

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, data):
        self.heap.append(data)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i-1)//2] > self.heap[i]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    def heapify(self, i):
        if self.heap:
            size = len(self.heap)

            while True:
                smallest = i
                left = (2*i)+1
                right = (2*i)+2

                if left < size and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < size and self.heap[right] < self.heap[smallest]:
                    smallest = right
                
                if smallest == i:
                    break

                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
        else:
            return
    
    def pop(self):
        if self.heap:
            min_val = self.heap[0]
            last_val = self.heap.pop()
            if self.heap:
                self.heap[0] = last_val
                self.heapify(0)
            return min_val
        else:
            return None
    
    def __str__(self):
        return str(self.heap)

heap = MinHeap()

for i in range(10):
    heap.push(random.randint(0, 100))

print(f"initial heap: {heap}\n")

for i in range(10):
    popped = heap.pop()
    print(f"popped: {popped};\theap: {heap}")