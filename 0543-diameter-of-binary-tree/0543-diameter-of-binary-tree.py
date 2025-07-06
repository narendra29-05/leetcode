# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def dia(root):
            if root is None:
                return 0
            lh=dia(root.left)
            rh=dia(root.right)
            self.maxi=max(lh+rh,self.maxi)
        
            return 1+ max(lh,rh)
        dia(root)
        return self.maxi
            