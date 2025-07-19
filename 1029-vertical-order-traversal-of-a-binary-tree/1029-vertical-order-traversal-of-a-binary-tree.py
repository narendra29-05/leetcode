# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=[]
        if not root:
            return []
        
        q=deque([(0,0,root)])
        while q:
            v,level,node=q.popleft()
            d.append((v,level,node.val))
            if node.left:
                q.append((v-1,level+1,node.left))
            if node.right:
                q.append((v+1,level+1,node.right))
        d.sort()
        res = []
        prev_col = float('-inf')
        for col, row, val in d:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)
        return res