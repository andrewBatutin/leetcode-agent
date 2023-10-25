
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, TreeNode):
            return False
        if self.val == __value.val:
            return True
        
    def __hash__(self) -> int:
        return hash(self.val)
    

def has_path(root: TreeNode, src: str, dst: str) -> bool:
    if not root:
        return False
    if not src:
        return False
    if src == dst:
        return True
    if root.left:
        if has_path(root.left, root.left.val, dst):
            return True
    if root.right:
        if has_path(root.right, root.right.val, dst):
            return True
    return False
    