# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inOrder = []

        def inOrderTraversal(node):
            if not node:
                return
            
            inOrderTraversal(node.left)
            inOrder.append(node)
            inOrderTraversal(node.right)
        
        inOrderTraversal(root)
        for i in inOrder:
            print(i.val)
        
        biggest = None
        nextSmall = None

        for i in range(len(inOrder) - 1):
            # print(inOrder[i].val)

            if inOrder[i].val > inOrder[i+1].val:
                if not biggest:
                    biggest = inOrder[i]
                nextSmall = inOrder[i + 1]
        
        
        if not biggest or not nextSmall:
            return 
        if biggest and nextSmall:
            biggest.val, nextSmall.val = nextSmall.val, biggest.val
        
            
        