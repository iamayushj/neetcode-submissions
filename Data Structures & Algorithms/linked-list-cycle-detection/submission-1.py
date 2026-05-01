# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            pointer1=head
            pointer2=head.next
        else:
            return False

        while pointer1 != pointer2:
            if not (pointer1 and pointer2 and pointer2.next):
                return False
            else:   
                pointer1 = pointer1.next
                pointer2 = pointer2.next.next
        return True