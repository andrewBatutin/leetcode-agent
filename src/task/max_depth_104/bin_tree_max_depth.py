from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
    


class Solution:

    queue_n = []

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0        
        
        self.queue_n.append(root.val)
        left_l = self.maxDepth(root.left)
        right_l = self.maxDepth(root.right)

        return 1 + max(left_l, right_l)
