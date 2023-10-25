from src.utils.utils import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        s = [(root, root.val)]
        good_count = 0
        while s:
            current, curr_max = s.pop()
            if current:
                if current.val >= curr_max:
                    good_count += 1
                    curr_max = current.val
                if current.left:
                    s.append((current.left, curr_max))
                if current.right:
                    s.append((current.right, curr_max))

        return good_count 
        