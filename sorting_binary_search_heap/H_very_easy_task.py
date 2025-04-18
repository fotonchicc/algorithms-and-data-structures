import sys


def binary_search(n, x, y):
    if n == 1:
        return min(x, y)
    left = 0
    right = (n - 1) * min(x, y)
    while right - left > 1:
        mid = (left + right) // 2
        if mid // x + mid // y >= n - 1:
            right = mid
        else:
            left = mid
    return min(x, y) + right


n, x, y = [int(value) for value in sys.stdin.readline().split()]
print(binary_search(n, x, y))
