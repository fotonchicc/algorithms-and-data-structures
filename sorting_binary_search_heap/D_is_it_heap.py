import sys
def is_heap(lst, n):
    if n == 1:
        return 'YES'
    lst = [None] + lst
    for i in range(1, n + 1):
        if 2 * i <= n:
            if lst[i] >= lst[2 * i]:
                return 'NO'
        if 2 * i + 1 <= n:
            if lst[i] >= lst[2 * i + 1]:
                return 'NO'

    return 'YES'


n = int(sys.stdin.readline().strip())
lst = [int(value) for value in sys.stdin.readline().split()]
res = is_heap(lst, n)
print(res)
