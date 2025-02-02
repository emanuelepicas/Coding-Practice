class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort linked list using merge sort
        Time: O(n log n)
        Space: O(log n) due to recursion
        """

        # Convert the linked list to array

        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        #This method utilize sort method already available for the array
        values.sort()

        dummy = ListNode(0)

        current = dummy
        
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next