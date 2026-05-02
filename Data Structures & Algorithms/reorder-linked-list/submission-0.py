# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1= head
        list2= head
        curr1=list1
        curr2=list2

        
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
        #if curr2 == None:
        list2 = curr1.next
        curr1.next = None

        prev = None
        curr3 = list2

        while curr3:
            nxt = curr3.next 
            curr3.next = prev 
            prev = curr3 
            curr3 = nxt 
        list2 = prev

        while list2:
            next1=list1.next
            next2=list2.next
            list1.next = list2
            list2.next = next1
            list1=next1
            list2=next2
        