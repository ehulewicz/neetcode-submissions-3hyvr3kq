# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def dfs(curr):
            if curr.left is not None:
                dfs(curr.left)
            
            in_order.append(curr.val)

            if curr.right is not None:
                dfs(curr.right)

        dfs(root)
        return in_order[k - 1]