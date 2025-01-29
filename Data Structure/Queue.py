class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return str(self.items)

# Visual Example:
"""
Initial: []
After enqueue(1): [1]
After enqueue(2): [1, 2]
After enqueue(3): [1, 2, 3]
After dequeue(): [2, 3]
"""

# Usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.front())  # 1
queue.dequeue()
print(queue.display())  # "[2, 3]"