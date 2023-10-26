import pytest

from src.task.count_good_nodes_1448.solution import Solution as Solution_1448
from src.task.leaf_sim_trees_872.solution import Solution as Solution_872
from src.task.max_depth_104.bin_tree_max_depth import Solution
from src.utils.utils import TreeNode, has_path, has_path_req


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


def test_bs_extraction():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.theguardian.com/technology/2023/feb/25/nokia-launches-diy-repairable-budget-android-phone"
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    metas = soup.find_all("meta")
    res = [
        meta.attrs["content"] for meta in metas if "property" in meta.attrs and "description" in meta.attrs["property"]
    ]
    print(res)


def test_slg():
    from slugify import slugify

    txt = "https://www.theguardian.com/technology/2023/feb/25/nokia-launches-diy-repairable-budget-android-phone"
    r = slugify(txt)
    assert r == "https-www-theguardian-com-technology-2023-feb-25-nokia-launches-diy-repairable-budget-android-phone"
