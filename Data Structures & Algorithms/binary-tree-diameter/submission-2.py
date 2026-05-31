# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    depth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def getDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            lh = getDepth(root.left)
            rh = getDepth(root.right)

            current = 1 + lh + rh
            self.depth = max(self.depth, current)
            return 1 + max(lh, rh)
        
        getDepth(root)
        return self.depth - 1