def binary_search(c):
    left = 1
    right = c
    eps = 10 ** -7
    while right - left > eps:
        mid = (left + right) / 2
        if mid ** 2 + mid ** 0.5 >= c:
            right = mid
        else:
            left = mid
    return right


c = float(input())
print(round(binary_search(c), 6))
