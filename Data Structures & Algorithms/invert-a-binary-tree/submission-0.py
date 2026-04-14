# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.helper(root)
        return root

    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        left = self.helper(root.right)
        right = self.helper(root.left)
        
        root.left = left
        root.right = right
        return root