import sys
from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None, size=1):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right
        self.size = size


def merge(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    if t1.priority > t2.priority:
        t1.right = merge(t1.right, t2)
        recalc(t1)
        return t1
    else:
        t2.left = merge(t1, t2.left)
        recalc(t2)
        return t2


def split(root, key, add=0):
    if root is None:
        return None, None
    cur_key = add + (root.left.size if root.left else 0) + 1
    if key < cur_key:
        left, root.left = split(root.left, key, add)
        recalc(root)
        return left, root
    else:
        root.right, right = split(root.right, key, cur_key)
        recalc(root)
        return root, right


def insert(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    sub_left = Vertex(key, randint(1, 100000))
    return merge(left_tree, merge(sub_left, sub_right))


def delete(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    return merge(left_tree, sub_right)


def recalc(v):
    if v:
        v.size = (1 + (v.left.size if v.left else 0) + (v.right.size if v.right else 0))


def find_kth(root, k, add=0):
    left_size = root.left.size if root.left else 0
    cur_key = add + left_size + 1
    if k == cur_key:
        return root.key
    elif k < cur_key:
        return find_kth(root.left, k, add)
    else:
        return find_kth(root.right, k, cur_key)


def build_tree(n):
    root = None
    for i in range(1, n + 1):
        root = merge(root, Vertex(i, randint(1, 100000)))
    return root


def main():
    n, m = list(map(lambda x: int(x), (sys.stdin.readline().split())))
    operations = [list(map(lambda x: int(x), st.split())) for st in sys.stdin.readlines()]
    tree = build_tree(n)
    for l, r in operations:
        left, mid_right = split(tree, l - 1)
        mid, right = split(mid_right, r - l + 1)
        tree = merge(mid, merge(left, right))
    result = [str(find_kth(tree, i + 1)) for i in range(n)]
    print(" ".join(result))


if __name__ == '__main__':
    main()
