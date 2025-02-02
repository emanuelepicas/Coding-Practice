# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Compare nodes from both lists and merge them in sorted order
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1                                
                print(f"Current ${current.next}")
                list1 = list1.next
                print(f"List1 ${list1}")
            else:
                current.next = list2
                print(f"Current list2 ${current.next}")
                list2 = list2.next


            current = current.next
        
        # If any list is remaining, append it to the end
        current.next = list1 if list1 else list2
        
        return dummy.next