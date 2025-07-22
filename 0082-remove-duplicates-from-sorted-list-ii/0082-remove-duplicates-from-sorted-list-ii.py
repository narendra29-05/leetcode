# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        countr=Counter(l)
        for i in l:
            if countr[i]==1:
                current.next=ListNode(i)
                current=current.next
        current.next=None
        return dummy.next
                
        

        