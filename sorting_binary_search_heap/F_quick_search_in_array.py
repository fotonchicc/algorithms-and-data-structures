import sys


def binary_search_left(lst, l):
    left = -1
    right = len(lst)
    while right - left > 1:
        mid = (left + right) // 2
        if mid < len(lst) and lst[mid] >= l:
            right = mid
        else:
            left = mid
    return right


def binary_search_right(lst, r):
    left = -1
    right = len(lst)
    while right - left > 1:
        mid = (left + right) // 2
        if mid < len(lst) and lst[mid] > r:
            right = mid
        else:
            left = mid
    return right


n = int(sys.stdin.readline().strip())
lst = [int(value) for value in sys.stdin.readline().split()]
k = int(sys.stdin.readline().strip())
requests = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

lst_sorted = sorted(lst)

res = []
for request in requests:
    left = binary_search_left(lst_sorted, request[0])
    right = binary_search_right(lst_sorted, request[1])
    values_number = right - left
    res.append(values_number)

print(*res)
