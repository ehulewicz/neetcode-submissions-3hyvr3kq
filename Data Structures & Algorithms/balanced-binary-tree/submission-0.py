# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def helper(curr: Optional[TreeNode]) -> int:
            nonlocal balanced
            if curr is None:
                return 0
            
            left = helper(curr.left)
            right = helper(curr.right)

            if abs(right - left) > 1:
                balanced = False

            return 1 + max(left, right)
        
        helper(root)
        return balanced