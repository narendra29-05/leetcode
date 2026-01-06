# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        ans=float("-inf")
        level=1
        order=1
        while q:
            n=len(q)
            # node=q.pop()
            sum=0
            for _ in range (n):
                node=q.popleft()
                sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if sum>ans:
                ans=sum
                order=level
            level+=1
        return order