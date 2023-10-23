import pytest

from src.task.max_depth_104.bin_tree_max_depth import Solution, TreeNode


@pytest.fixture
def mock_adj_list():
    return {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": [], "e": ["b"], "f": ["d"]}


@pytest.fixture
def mock_tree(mock_adj_list, root="a"):
    return convert_to_tree(mock_adj_list, root)


def convert_to_tree(adj_list, root):
    if not root:
        return None
    tree = TreeNode(val=root)
    if root in adj_list:
        children = adj_list[root]
        if len(children) > 0:
            tree.left = convert_to_tree(adj_list, children[0])
        if len(children) > 1:
            tree.right = convert_to_tree(adj_list, children[1])
    return tree


def test_104(mock_tree):
    s = Solution()
    assert s.maxDepth(mock_tree) == 5
