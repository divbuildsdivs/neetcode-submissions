# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def addNodes(root):
            if root == None:
                return
            addNodes(root.left)
            addNodes(root.right)
            res.append(root.val)
        addNodes(root)
        return res
