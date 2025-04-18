import sys
n = int(sys.stdin.readline().strip())
lst = [list(map(lambda x: int(x), value.split())) for value in sys.stdin.readlines()]
tree = lst[:-1]
root_inx = lst[-1][0] - 1

def is_bst(node):
    data, l, r = tree[node]
    if l == -1 and r == -1:
        return True
    elif l == -1:
        if not data < tree[r - 1][0]:
            return False
        return is_bst(r - 1)
    elif r == -1:
        if not tree[l - 1][0] < data:
            return False
        return is_bst(l - 1)
    else:
        if not tree[l - 1][0] < data < tree[r - 1][0]:
            return False
        return is_bst(l - 1) and is_bst(r - 1)


print("YES" if is_bst(root_inx) else "NO")

