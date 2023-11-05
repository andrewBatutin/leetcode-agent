from typing import Optional
from src.utils.utils import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.t_sum = targetSum
        self.n_count = 0
        s = [root]
        
        while s:

            current = s.pop()
    
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)

            self.traverse(current, 0)
        return self.n_count
    
    def traverse(self, root, sum):
        if not root:
            return
        sum += root.val
        if sum == self.t_sum:
            self.n_count += 1
        self.traverse(root.left, sum)
        self.traverse(root.right, sum)

