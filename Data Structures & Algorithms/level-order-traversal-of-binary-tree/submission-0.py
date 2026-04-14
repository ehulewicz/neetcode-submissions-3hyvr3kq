# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = [root]
        traversal = []

        while level:
            level_values = []
            next_level = []
            for n in level:
                if not n:
                    continue

                level_values.append( n.val )
                if n.left:
                    next_level.append( n.left )
                if n.right:
                    next_level.append( n.right )
            
            if level_values:
                traversal.append( level_values )
            level = next_level


        return traversal
            