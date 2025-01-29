class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)
    
    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        if current.next:
            current.next = current.next.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.val))
            current = current.next
        return " -> ".join(elements)

# Visual Example:
"""
Initial: None
After insert(1): 1 -> None
After insert(2): 1 -> 2 -> None
After insert(3): 1 -> 2 -> 3 -> None
After delete(2): 1 -> 3 -> None
"""

# Usage:
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print(ll.display())  # "1 -> 2 -> 3"
ll.delete(2)
print(ll.display())  # "1 -> 3"