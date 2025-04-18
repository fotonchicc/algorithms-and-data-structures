import sys


def check(lst, x, mid):
    return lst[mid] > x


def binary_search(lst, x):
    left = 0
    right = len(lst)
    while right - left > 1:
        mid = (left + right) // 2
        if check(lst, x, mid):
            right = mid
        else:
            left = mid
    if right == len(lst):
        return left
    elif abs(x - lst[left]) - abs(x - lst[right]) < eps:
        return left
    elif abs(x - lst[left]) < abs(x - lst[right]):
        return left
    else:
        return right


n, k = [int(value) for value in sys.stdin.readline().split()]
lst = [int(value) for value in sys.stdin.readline().split()]
requests = [int(value) for value in sys.stdin.readline().split()]

eps = 10 ** -7


for request in requests:
    closest = binary_search(lst, request)
    print(lst[closest])
