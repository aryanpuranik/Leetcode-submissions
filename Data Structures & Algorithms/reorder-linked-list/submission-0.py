# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val 
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next

        #reverse

        prev= None
        slow.next=None
        while second:
            
            tmp= second.next
            second.next = prev
            prev=second
            second= tmp
            
        #merge
        second = prev

        while second:
            temp1 = head.next
            temp2 = second.next
            head.next = second
            second.next = temp1
            head = temp1
            second = temp2
        
