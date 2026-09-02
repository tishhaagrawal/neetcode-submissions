# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height_left = self.height(root.left)
        height_right = self.height(root.right)
        diameter = height_left + height_right

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(sub, diameter)

        
        