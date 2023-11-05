import pytest

from src.task.count_good_nodes_1448.solution import Solution as Solution_1448
from src.task.leaf_sim_trees_872.solution import Solution as Solution_872
from src.task.max_depth_104.bin_tree_max_depth import Solution
from src.task.path_sum_3_437.solution import Solution as Solution_437
from src.utils.utils import TreeNode, build_graph, connected_component_count, has_path, has_path_req, undir_path


@pytest.fixture
def mock_adj_list_1448_2():
    # [2,null,4,10,8,null,null,4]

    root = TreeNode(
        val=2,
        left=TreeNode(val=1, left=None, right=None),
        right=TreeNode(
            val=4,
            left=TreeNode(val=10, left=None, right=None),
            right=TreeNode(val=8, left=None, right=TreeNode(val=4, left=None, right=None)),
        ),
    )
    return root


@pytest.fixture
def mock_adj_list_1448():
    list_flat = [3, 2, 4, 6, None, 1, 5]
    adj_list = convert_list_adj_list(list_flat)
    return convert_to_tree(adj_list=adj_list, root=list_flat[0])


@pytest.fixture
def mock_adj_list_left_sim_1():
    list_flat = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    adj_list = convert_list_adj_list(list_flat)
    return convert_to_tree(adj_list=adj_list, root=list_flat[0])


@pytest.fixture
def mock_adj_list_left_sim_2():
    list_flat = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    adj_list = convert_list_adj_list(list_flat)
    return convert_to_tree(adj_list=adj_list, root=list_flat[0])


def convert_list_adj_list(list_bin):
    adj_list = {}
    i_2 = 1
    for i in range(0, len(list_bin) // 2):
        adj_list[list_bin[i]] = [list_bin[i_2], list_bin[i_2 + 1]]
        i_2 += 2
    return adj_list


@pytest.fixture
def mock_adj_list():
    return {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


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
    assert s.maxDepth(mock_tree) == 4


def test_depth_first(mock_tree):
    s = Solution()
    s.depth_first(mock_tree)
    assert s.res == ["a", "b", "d", "f", "c", "e"]
    s = Solution()
    s.depth_first_recursive(mock_tree)
    assert s.res == ["a", "b", "d", "f", "c", "e"]


def test_depth_first_recursive(mock_tree):
    s = Solution()
    s.depth_first_recursive(mock_tree)
    assert s.res == ["a", "b", "d", "f", "c", "e"]


def test_breadth_first(mock_tree):
    s = Solution()
    s.breadth_first(mock_tree)
    assert s.res == ["a", "b", "c", "d", "e", "f"]


def test_left_sim(mock_adj_list_left_sim_1, mock_adj_list_left_sim_2):
    s = Solution_872()
    res = s.leafSimilar(mock_adj_list_left_sim_1, mock_adj_list_left_sim_2)
    assert res is True


def test_has_path_req(mock_tree):
    res = has_path_req(mock_tree, "a", "f")
    assert res is True
    res = has_path_req(mock_tree, "a", "e")
    assert res is True


def test_has_no_path_req(mock_tree):
    res = has_path_req(mock_tree, "a", "z")
    assert res is False


def test_has_path(mock_tree):
    res = has_path(mock_tree, "a", "f")
    assert res is True
    res = has_path(mock_tree, "a", "e")
    assert res is True


def test_has_no_path(mock_tree):
    res = has_path(mock_tree, "a", "z")
    assert res is False


def test_count_good_nodes(mock_adj_list_1448_2):
    s = Solution_1448()
    res = s.goodNodes(mock_adj_list_1448_2)
    assert res == 4


def test_graph_conv():
    edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
    graph = build_graph(edges)
    expected = {"i": ["j", "k"], "j": ["i"], "k": ["i", "m", "l"], "m": ["k"], "l": ["k"], "o": ["n"], "n": ["o"]}
    assert graph == expected


def test_is_und_path():
    edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
    is_path = undir_path(edges, "i", "l")
    assert is_path is True


def test_no_is_und_path():
    edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
    is_path = undir_path(edges, "i", "n")
    assert is_path is False


def test_path_sum_3():
    root = TreeNode(
        val=10,
        left=TreeNode(
            val=5,
            left=TreeNode(
                val=3, left=TreeNode(val=3, left=None, right=None), right=TreeNode(val=-2, left=None, right=None)
            ),
            right=TreeNode(val=2, left=None, right=TreeNode(val=1, left=None, right=None)),
        ),
        right=TreeNode(val=-3, right=TreeNode(val=11, left=None, right=None)),
    )
    s = Solution_437()

    res = s.pathSum(root, 8)
    assert res == 3


def test_connected_comp():
    tree = TreeNode(
        val=0,
        left=TreeNode(
            val=8,
            left=TreeNode(val=0, left=None, right=None),
            right=TreeNode(
                val=5, left=TreeNode(val=0, left=None, right=None), right=TreeNode(val=8, left=None, right=None)
            ),
        ),
        right=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None), right=None),
    )

    c = connected_component_count(tree)
    assert c == 2
