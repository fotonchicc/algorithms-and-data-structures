import sys
from random import randint


class Vertex():
    def __init__(self, key=None, priority=None, left=None, right=None, index=None):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right
        self.index = index
        self.nodes = []

    def __str__(self):
        result = []
        for node in self.nodes:
            l_index = node.left.index if node.left else -1
            r_index = node.right.index if node.right else -1
            result.append(f"{node.key} {l_index} {r_index}")
        result.append("1")
        return "\n".join(result)

    def collect_nodes(self):
        stack = [self]
        while stack:
            node = stack.pop()
            self.nodes.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def merge(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    if t1.priority < t2.priority:
        t1.right = merge(t1.right, t2)
        return t1
    else:
        t2.left = merge(t1, t2.left)
        return t2


def split(root, key):
    if root is None:
        return None, None
    if root.key < key:
        (root.right, right_tree) = split(root.right, key)
        return root, right_tree
    else:
        (left_tree, root.left) = split(root.left, key)
        return left_tree, root


def insert(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    new_node = Vertex(key, randint(1000, 9999))
    return merge(left_tree, merge(new_node, sub_right))


def main():
    n = int(sys.stdin.readline().strip())
    tree_data = [int(value) for value in sys.stdin.readline().split()]
    tree = None
    for vertex in tree_data:
        tree = insert(tree, vertex)

    if tree:
        tree.collect_nodes()
        for idx, node in enumerate(tree.nodes):
            node.index = idx + 1

    print(n)
    print(tree)


if __name__ == '__main__':
    main()
