class Array:
    def __init__(self):
        self.arr = []
        
    def insert(self, val):
        self.arr.append(val)
        
    def delete(self, index):
        if 0 <= index < len(self.arr):
            return self.arr.pop(index)
        return None
        
    def get(self, index):
        if 0 <= index < len(self.arr):
            return self.arr[index]
        return None

# Visual Example:
"""
Initial: []
After insert(1): [1]
After insert(2): [1, 2]
After insert(3): [1, 2, 3]
After delete(1): [1, 3]
"""

# Usage:
arr = Array()
arr.insert(1)  # [1]
arr.insert(2)  # [1, 2]
arr.insert(3)  # [1, 2, 3]
print(arr.get(1))  # 2
arr.delete(1)  # [1, 3]