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

    def __init__(self) -> None:
        self.res = []

    def has_path(self, src: Optional[TreeNode], dst: Optional[TreeNode]):
        pass

    def breadth_first(self, root: Optional[TreeNode]):
        q = [root]

        while q:
            current = q.pop(0)
            self.res.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
    

    def depth_first(self, root: Optional[TreeNode]):
        s_stack = [root]

        while s_stack:
            current = s_stack.pop() #  this is the only difference between breadth and depth first, pop vs pop(0)
            print(current.val)
            self.res.append(current.val)
            if current.right:
                s_stack.append(current.right)
            if current.left:
                s_stack.append(current.left)

    
    def depth_first_recursive(self, root: Optional[TreeNode]):
        
        if root is None:
            return
        print(root.val)
        self.res.append(root.val)
        self.depth_first_recursive(root.left)
        self.depth_first_recursive(root.right)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0        
        
        self.queue_n.append(root.val)
        left_l = self.maxDepth(root.left)
        right_l = self.maxDepth(root.right)

        return 1 + max(left_l, right_l)
