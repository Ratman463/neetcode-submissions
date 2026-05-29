# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        def heightOfTree(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            lh = heightOfTree(root.left)
            rh = heightOfTree(root.right)
            self.diameter = max(self.diameter, lh + rh)
            return 1 + max(lh, rh)
        
        heightOfTree(root)
        return self.diameter