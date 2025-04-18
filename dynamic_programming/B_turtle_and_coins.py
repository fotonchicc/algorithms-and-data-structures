import sys

n, m = map(int, sys.stdin.readline().split())
coins = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[-float("inf")] * m for _ in range(n)]
prev = [[-1] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[0][0] = coins[0][0]
            prev[0][0] = -1
        elif i == 0:
            dp[0][j] = dp[0][j - 1] + coins[0][j]
            prev[0][j] = 1
        elif j == 0:
            dp[i][0] = dp[i - 1][0] + coins[i][0]
            prev[i][0] = 0
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + coins[i][j]
            if dp[i - 1][j] > dp[i][j - 1]:
                prev[i][j] = 0
            else:
                prev[i][j] = 1

path = []
i, j = n - 1, m - 1
while i > 0 or j > 0:
    if prev[i][j] == 1:
        path.append("R")
        j -= 1
    else:
        path.append("D")
        i -= 1

path.reverse()

print(dp[n - 1][m - 1])
print("".join(path))
