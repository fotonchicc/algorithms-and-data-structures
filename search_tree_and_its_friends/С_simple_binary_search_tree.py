import sys
from random import randint


class Vertex:
    def __init__(self, key=None, priority=None, left=None, right=None):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right


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
    new_node = Vertex(key, randint(1, 9999))
    return merge(left_tree, merge(new_node, sub_right))


def exists(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    is_exists = sub_left is not None
    return "true" if is_exists else "false", merge(left_tree, merge(sub_left, sub_right))


def delete(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    return merge(left_tree, sub_right)


def find_next(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    if sub_right is None:
        next_key = "none"
    else:
        current = sub_right
        while current.left is not None:
            current = current.left
        next_key = current.key
    return next_key, merge(left_tree, merge(sub_left, sub_right))


def find_prev(root, key):
    (left_tree, right_tree) = split(root, key)
    (sub_left, sub_right) = split(right_tree, key + 1)
    if left_tree is None:
        prev_key = "none"
    else:
        current = left_tree
        while current.right is not None:
            current = current.right
        prev_key = current.key
    return prev_key, merge(left_tree, merge(sub_left, sub_right))


def main():
    operations = [list(str.split()) for str in sys.stdin.readlines()]
    tree = None
    for operation in operations:
        action = operation[0]
        key = int(operation[1])
        match action:
            case "insert":
                tree = insert(tree, key)
            case "exists":
                flag, tree = exists(tree, key)
                print(flag)
            case "next":
                next, tree = find_next(tree, key)
                print(next)
            case "prev":
                prev, tree = find_prev(tree, key)
                print(prev)
            case "delete":
                tree = delete(tree, key)


if __name__ == '__main__':
    main()
