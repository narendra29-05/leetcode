"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        l=[]
        if root is None:
            return l
        q=deque([root])
        while q:
            n=len(q)
            e=[]
            for _ in range (n):
                
                node=q.popleft()
                for c in  node.children:
                    q.append(c)
                e.append(node.val)
            l.append(e)
        return l
                

