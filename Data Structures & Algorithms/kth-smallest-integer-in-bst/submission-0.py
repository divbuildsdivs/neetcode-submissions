# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minnodes = []

        def addNodes(root):
            if root == None:
                return
            addNodes(root.left)
            minnodes.append(root.val)
            addNodes(root.right)
        addNodes(root)
        print(minnodes)
        return minnodes[k - 1]

        