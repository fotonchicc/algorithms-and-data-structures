import sys
def counting_sort(lst, max, n):
    lst_values = [0] * (max + 1)
    for i in range(0, n):
        lst_values[lst[i]] += 1
    k = 0
    for j in range(0, max + 1):
        while lst_values[j] > 0:
            lst[k] = j
            lst_values[j] -= 1
            k += 1
        j += 1
    return lst

n = int(sys.stdin.readline().strip())
lst = [int(value) for value in sys.stdin.readline().split()]

lst_sorted = counting_sort(lst, 100, n)
print(*lst_sorted)
