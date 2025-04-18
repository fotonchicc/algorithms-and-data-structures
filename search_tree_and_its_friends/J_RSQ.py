import sys
from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None, size=1):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right
        self.size = size
        self.subtree_sum = key if key is not None else 0


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


def recalc(v):
    if v:
        v.size = (1 + (v.left.size if v.left else 0) + (v.right.size if v.right else 0))
        v.subtree_sum = (v.key if v.key is not None else 0) + \
                        (v.left.subtree_sum if v.left else 0) + \
                        (v.right.subtree_sum if v.right else 0)


def set_value(root, i, x, add=0):
    if root is None:
        return
    left_size = root.left.size if root.left else 0
    cur_pos = add + left_size + 1
    if i == cur_pos:
        root.key = x
        recalc(root)
    elif i < cur_pos:
        set_value(root.left, i, x, add)
        recalc(root)
    else:
        set_value(root.right, i, x, cur_pos)
        recalc(root)


def build_tree(m):
    root = None
    for i in m:
        root = merge(root, Vertex(i, randint(1, 100000)))
    return root

def count_sum(root, i, j):
    left_tree, mid_tree = split(root, i - 1)
    mid_tree, right_tree = split(mid_tree, j - i + 1)
    sm = mid_tree.subtree_sum if mid_tree else 0
    root = merge(left_tree, merge(mid_tree, right_tree))
    return sm, root


def main():
    input = sys.stdin.read().splitlines()
    n = int(input[0])
    arr = list(map(lambda x: int(x), input[1].split()))
    operations = [list(st.split()) for st in input[2:]]
    tree = build_tree(arr)
    for operation in operations:
        action = operation[0]
        match action:
            case 'set':
                i, x = int(operation[1]), int(operation[2])
                set_value(tree, i, x)
            case 'sum':
                i, j = int(operation[1]), int(operation[2])
                sm, tree = count_sum(tree, i, j)
                print(sm)


if __name__ == '__main__':
    main()
