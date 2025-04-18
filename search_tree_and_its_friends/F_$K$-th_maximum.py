import sys
from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None, size=1):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right
        self.subtree_size = size


def merge(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    if t1.priority < t2.priority:
        t1.right = merge(t1.right, t2)
        recalc(t1)
        return t1
    else:
        t2.left = merge(t1, t2.left)
        recalc(t2)
        return t2


def split(root, key):
    if root is None:
        return None, None
    if root.key < key:
        (root.right, right_tree) = split(root.right, key)
        recalc(root)
        return root, right_tree
    else:
        (left_tree, root.left) = split(root.left, key)
        recalc(root)
        return left_tree, root


def insert(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    if sub_left is None:
        sub_left = Vertex(key, randint(1, 100000))
    return merge(left_tree, merge(sub_left, sub_right))


def delete(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    return merge(left_tree, sub_right)


def recalc(v):
    if v:
        v.subtree_size = (1 + (v.left.subtree_size if v.left else 0) + (v.right.subtree_size if v.right else 0))


def find_kth_max(root, k):
    right_size = root.right.subtree_size if root.right else 0
    if k == right_size + 1:
        return root.key
    elif k <= right_size:
        return find_kth_max(root.right, k)
    else:
        return find_kth_max(root.left, k - right_size - 1)


def main():
    n = int(sys.stdin.readline())
    operations = [list(map(lambda x: int(x), str.split())) for str in sys.stdin.readlines()]
    tree = None
    for operation in operations:
        action = operation[0]
        key = operation[1]
        match action:
            case 1:
                tree = insert(tree, key)
            case 0:
                kth_max = find_kth_max(tree, key)
                print(kth_max)
            case -1:
                tree = delete(tree, key)


if __name__ == '__main__':
    main()
