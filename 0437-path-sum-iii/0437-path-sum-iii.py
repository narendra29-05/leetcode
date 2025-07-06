from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def path(node, target):
            if not node:
                return 0

            count = 0
            q = deque([(node, 0)])  # Each element: (current node, current sum)
            while q:
                current, curr_sum = q.popleft()
                curr_sum += current.val
                if curr_sum == target:
                    count += 1
                if current.left:
                    q.append((current.left, curr_sum))
                if current.right:
                    q.append((current.right, curr_sum))
            return count

        # Count paths starting from current root
        total = path(root, targetSum)
        # Recurse on left and right
        total += self.pathSum(root.left, targetSum)
        total += self.pathSum(root.right, targetSum)
        return total
