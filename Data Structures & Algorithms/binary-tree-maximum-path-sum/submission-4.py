# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = 0 - sys.maxsize

        def maxSumForNode(node):
            nonlocal maxSum
            if not node:
                return 0
            leftMax = node.val + maxSumForNode(node.left)
            rightMax =  node.val + maxSumForNode(node.right)
            totalSum = leftMax + rightMax - node.val
            maxSumForCurrent = max(leftMax, rightMax, totalSum, node.val)
            maxSum = max(maxSum, maxSumForCurrent)

            return max(leftMax, rightMax, node.val)
        
        maxSumForNode(root)
        return maxSum


        