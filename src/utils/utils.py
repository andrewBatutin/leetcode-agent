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


def has_path_req(root: TreeNode, src: str, dst: str) -> bool:
    if not root:
        return False
    if not src:
        return False
    if src == dst:
        return True
    if root.left:
        if has_path_req(root.left, root.left.val, dst):
            return True
    if root.right:
        if has_path_req(root.right, root.right.val, dst):
            return True
    return False


def has_path(root: TreeNode, src: str, dst: str) -> bool:
    q = [root]

    while q:
        current = q.pop(0)
        if current.val == dst:
            return True
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return False


def build_graph(edges: list) -> dict:
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


def undir_path(edges, node_a, node_b):
    graph = build_graph(edges)
    visited = set()
    return has_path_rec(graph, node_a, node_b, visited)


def has_path_rec(edges, src, dst, visited):
    if src in visited:
        return False
    if src == dst:
        return True
    visited.add(src)
    for neighbor in edges[src]:
        if has_path_rec(edges, neighbor, dst, visited):
            return True

    return False


def connected_component_count(root: TreeNode):
    visited = set()
    count = 0
    if root.left:
        if explore(root.left, visited):
            count += 1
    if root.right:
        if explore(root.right, visited):
            count += 1

    return count


def explore(current: TreeNode, visited: set):
    if current.val in visited:
        return False

    visited.add(current.val)

    if current.left:
        explore(current.left, visited)
    if current.right:
        explore(current.right, visited)

    return True
