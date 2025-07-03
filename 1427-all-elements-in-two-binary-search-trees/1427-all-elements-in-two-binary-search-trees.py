# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        if not root1 and not root2:
            return []
        def dfs(root):
            if root:
                l.append(root.val)
            if not root :
                return
            dfs(root.left)
            dfs(root.right)
        l=[]
        dfs(root1)
        dfs(root2)
        return sorted(l)
        