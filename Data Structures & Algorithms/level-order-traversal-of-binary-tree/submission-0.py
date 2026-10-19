# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if root != None:
            queue.append(root)
        while len(queue) != 0:
            N = len(queue)
            curr = []
            for i in range(N):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:  
                    queue.append(node.right)
                curr.append(node.val)
            res.append(curr)
        return res


        