import sys
from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right
        self.subtree_sum = key if key is not None else 0


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

def recalc(v):
    if v:
        v.subtree_sum = (v.key if v.key is not None else 0) + \
                        (v.left.subtree_sum if v.left else 0) + \
                        (v.right.subtree_sum if v.right else 0)


def find_sum(root, l, r):
    left_tree, mid_tree = split(root, l)
    mid_tree, right_tree = split(mid_tree, r + 1)
    sum = mid_tree.subtree_sum if mid_tree else 0
    root = merge(left_tree, merge(mid_tree, right_tree))
    return sum, root


def main():
    n = int(sys.stdin.readline())
    operations = [list(str.split()) for str in sys.stdin.readlines()]
    tree = None
    y = None
    for i, operation in enumerate(operations):
        action = operation[0]
        match action:
            case "+":
                key = int(operation[1])
                if tree is None:
                    tree = insert(tree, key)
                elif operations[i - 1][0] == "+":
                    tree = insert(tree, key)
                else:
                    key = (key + y) % 10 ** 9
                    tree = insert(tree, key)
            case "?":
                l = int(operation[1])
                r = int(operation[2])
                y, tree = find_sum(tree, l, r)
                print(y)



if __name__ == '__main__':
    main()
