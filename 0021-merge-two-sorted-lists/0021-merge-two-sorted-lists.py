# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Step 1: Create a dummy node to anchor the start of the new list
        dummy = ListNode()
        tail = dummy
        
        # Step 2: Loop while both lists have nodes left
        while list1 and list2:
            # Step 3: Compare values and link the smaller one
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next  # Move list1 forward
            else:
                tail.next = list2
                list2 = list2.next  # Move list2 forward
            
            # Step 4: Advance the tail pointer
            tail = tail.next
        
        # Step 5: Attach whatever is left over from whichever list didn't finish
        tail.next = list1 if list1 else list2
        
        # Step 6: Return everything after the dummy placeholder
        return dummy.next