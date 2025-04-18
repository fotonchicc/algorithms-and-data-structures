import sys

def merge_list(a, b):
    merge_lst = []
    inversions_number = 0
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
            inversions_number += size_first - i
    merge_lst.extend(a[i:])
    merge_lst.extend(b[k:])
    return merge_lst, inversions_number


def split(lst):
    if len(lst) < 2:
        return lst, 0
    size_one = len(lst) // 2
    a = lst[:size_one]
    b = lst[size_one:]
    left_sorted, left_inversions = split(a)
    right_sorted, right_inversions = split(b)
    merged, merge_inversions = merge_list(left_sorted, right_sorted)
    total_inversions = left_inversions + right_inversions + merge_inversions
    return merged, total_inversions


n = int(sys.stdin.readline().strip())
lst = [int(value) for value in sys.stdin.readline().split()]
lst_sorted, inversions = split(lst)
print(inversions)
