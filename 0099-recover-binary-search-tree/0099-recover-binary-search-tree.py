
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first=self.prev=self.second=None
        def inorder(node):
            if not node:
                return True
            inorder(node.left)
            if self.prev and node.val<self.prev.val:
                if not self.first:
                    self.first=self.prev
                self.second=node
            self.prev = node
            inorder(node.right)
        
        self.prev = TreeNode(float('-inf'))
        inorder(root)
        
        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val