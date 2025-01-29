class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return str(self.items)

# Visual Example:
"""
Initial: []
After push(1): [1]
After push(2): [1, 2]
After push(3): [1, 2, 3]
After pop(): [1, 2]
"""

# Usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # 3
stack.pop()
print(stack.display())  # "[1, 2]"