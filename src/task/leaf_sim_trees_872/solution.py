from typing import Optional
from src.utils.utils import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list_1 = []
        list_2 = []
        queue_1 = [root1]
        queue_2 = [root2]

        while queue_1:
            current = queue_1.pop()
            
            if (current.left is None) & (current.right is None):
                list_1.append(current.val)

            if current.left:
                queue_1.append(current.left)

            if current.right:
                queue_1.append(current.right)

        while queue_2:
            current = queue_2.pop()
            
            if (current.left is None) & (current.right is None):
                list_2.append(current.val)

            if current.left:
                queue_2.append(current.left)

            if current.right:
                queue_2.append(current.right)


        return list_1 == list_2