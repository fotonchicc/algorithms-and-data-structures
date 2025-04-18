import sys

def merge_list(a, b):
    merge_lst = []
    size_first = len(a)
    size_second = len(b)
    i = 0
    k = 0
    while i < size_first and k < size_second:
        if a[i] <= b[k]:
            merge_lst.append(a[i])
            i += 1
        else:
            merge_lst.append(b[k])
            k += 1
    merge_lst.extend(a[i:])
    merge_lst.extend(b[k:])
    return merge_lst

def split(lst):
    size_one = len(lst) // 2
    a = lst[:size_one]
    b = lst[size_one:]
    if len(a) > 1:
        a = split(a)
    if len(b) > 1:
        b = split(b)

    return merge_list(a, b)

n = int(sys.stdin.readline().strip())
lst = [int(value) for value in sys.stdin.readline().split()]
lst_sorted = split(lst)
print(*lst_sorted)
