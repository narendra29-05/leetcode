class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        def path(c_s,stack,node):
            if node is None:
                return 
            c_s+=node.val
            stack.append(node.val)
            if node.left is None and node.right is None and c_s==targetSum:
                l.append(stack[:])
                
            path(c_s,stack,node.left)
            path(c_s,stack,node.right)
            stack.pop()
        l=[]
        path(0,[],root)
        return l