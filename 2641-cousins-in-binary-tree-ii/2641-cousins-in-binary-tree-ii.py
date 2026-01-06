# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None
        root.val=0
        q=deque([root])
        copy=root
        while q:
            n=len(q)
            copy_q=deque(q)
            sum=0
            for _ in range (n):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    sum+=node.left.val
                if node.right:
                    q.append(node.right)
                    sum+=node.right.val
            for _ in range (n):
                node=copy_q.popleft()
                current_sum=0
                if node.left:
                    current_sum+=node.left.val
                if node.right:
                    current_sum+=node.right.val
                if node.left:
                    node.left.val=sum-current_sum
                if node.right:
                    node.right.val=sum-current_sum
        return copy
            


        