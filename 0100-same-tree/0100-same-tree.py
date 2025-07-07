# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def inorder(root,l):
            if root is None:
                return
            if root.left is None:
                l.append(0)
            if root.right is None:
                l.append(0)
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
            print(l)
            return l
        l=[]
        r=[]
        return inorder(p,l)==inorder(q,r)