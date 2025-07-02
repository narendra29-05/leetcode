# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_length(root):
            if not root:
                return 0

            q=deque([root])
            c=0
            while q:
                n=len(q)
                for _ in range (n):
                    node=q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                c+=1
            return c
        if not root :
            return True
        left=check_length(root.left)
        right=check_length(root.right)
        if abs(right-left)>1 :
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
