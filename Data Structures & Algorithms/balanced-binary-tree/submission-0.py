# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return -1 <= (self.checkHeight(root.left) - self.checkHeight(root.right)) <=1 
        return False

    def checkHeight(self, curr):
            if not curr:
                return 0
            left = self.checkHeight(curr.left)
            right = self.checkHeight(curr.right)

            return 1 + max(left, right)
        
        
        