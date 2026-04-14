from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if self.check(curr, subRoot):
                return True
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False


    def check(self, node, subNode):
        if not node and not subNode:
            return True
        if not node or not subNode:
            return False
        if node.val != subNode.val:
            return False
        return self.check(node.left, subNode.left) and self.check(node.right, subNode.right)