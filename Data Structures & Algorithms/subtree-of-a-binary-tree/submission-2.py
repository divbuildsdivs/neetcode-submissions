# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

      queue = deque()
      queue.append(root)
      def checkSubtree(root1, root2):
        if root1 == None and root2 == None:
          return True
        if root1 == None or root2 == None:
          return False

        if root1.val != root2.val:
          return False
        else:
          return checkSubtree(root1.left, root2.left) & checkSubtree(root1.right, root2.right)

      while len(queue) > 0:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.val == subRoot.val:
                if checkSubtree(node, subRoot):
                  return True
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
            
      return False