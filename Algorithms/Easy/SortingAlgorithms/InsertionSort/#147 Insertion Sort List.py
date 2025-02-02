# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort linked list using insertion sort
        Time: O(n²)
        Space: O(1)
        """
        if not head or not head.next:
            return head
            
        # Create dummy node to handle insertion at beginning
        dummy = ListNode(0)
        curr = head

        print(f"Current list {curr}\n")
        iteration = 0
        while curr:
            print(f"Iteration Number {iteration}\n")
            # Keep track of next node to process
            next_node = curr.next
            
            # Find insertion position
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                print(f"Iterating the list {prev} \n")
                prev = prev.next
            
            # Insert current node and deletion of the node 4 from the original list
            print(f"Current next {curr.next}\n")
            curr.next = prev.next
            print(f"Current dummy next {prev.next}\n")
            prev.next = curr
            print(f"Current Dummy node {prev} and dummy node.next {prev.next}\n")
            print(f"Current before deletion list {curr}\n")
            # Move to next node
            curr = next_node
            print(f"Current after deletion and connected list {curr}\n")
            iteration += 1
            
        return dummy.next