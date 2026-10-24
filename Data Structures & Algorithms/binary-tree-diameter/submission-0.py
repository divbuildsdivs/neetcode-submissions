# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            leftheight = dfs(curr.left)
            rightheight = dfs(curr.right)
            res = max(res, leftheight + rightheight)

            return 1 + max(leftheight, rightheight)
        
        dfs(root)
        return res
        