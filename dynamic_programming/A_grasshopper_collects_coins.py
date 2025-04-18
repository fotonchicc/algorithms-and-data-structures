import sys

n, k = map(int, sys.stdin.readline().split())
coins_per_column = [0] + list(map(int, sys.stdin.readline().split())) + [0]
dp = [-float("inf")] * n
prev = [-1] * n

dp[0] = 0
for i in range(1, n):
    for j in range(max(0, i - k), i):
        if dp[j] + coins_per_column[i] > dp[i]:
            dp[i] = dp[j] + coins_per_column[i]
            prev[i] = j

path = []
cur = n - 1
while cur != -1:
    path.append(cur + 1)
    cur = prev[cur]

path.reverse()

print(dp[n - 1])
print(len(path) - 1)
print(*path)
