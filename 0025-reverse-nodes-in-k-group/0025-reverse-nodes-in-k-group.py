# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
            def rev(head):
                b=None
                while head:
                    a=head
                    head=head.next
                    a.next=b
                    b=a
                return b
            if head is None:
                return head
            temp=head
            headcopy=head
            c=k
            first=head
            while temp.next and c>1:
                c-=1
                temp=temp.next
            if c==1:
                second=temp.next
                temp.next=None
                first=rev(head)
                headcopy.next=self.reverseKGroup(second,k)
            return first
            

                
            