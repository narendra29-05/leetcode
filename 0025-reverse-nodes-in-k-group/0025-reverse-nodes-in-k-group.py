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
            c=k
            temp=head
            headcopy=head
            copy=head
            while c>1 and temp.next:
                temp=temp.next
                c-=1
            if c==1:
                link=temp.next
                temp.next=None
                copy=rev(copy)
                headcopy.next=self.reverseKGroup(link,k)
            return copy



        