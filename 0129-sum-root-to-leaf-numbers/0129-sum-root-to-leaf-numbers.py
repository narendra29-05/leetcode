# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def path(root):
            if root is None:
                return
            if root.right is None and root.left is None:
                l.append(root.val)
                return
            
            if root.left:
                root.left.val=(root.val*10)+(root.left.val)
                path(root.left) 
            if root .right:
                root.right.val=(root.val*10)+(root.right.val)   
                path(root.right) 
        l=[]
        path(root)
        return sum(l)
                    