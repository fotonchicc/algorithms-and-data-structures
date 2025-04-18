import sys

n = int(sys.stdin.readline())

MOD = 10 ** 9

moves = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}

dp = [[0] * 10 for _ in range(n + 1)]

for j in range(1, 10):
    if j != 8:
        dp[1][j] = 1

for i in range(1, n):
    for j in range(10):
        for next in moves[j]:
            dp[i + 1][next] = (dp[i + 1][next] + dp[i][j]) % MOD

res = sum(dp[n][j] for j in range(10)) % MOD

print(res)


