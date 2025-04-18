import sys

s1 = sys.stdin.readline()
s2 = sys.stdin.readline()

l1 = len(s1)
l2 = len(s2)

dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(l1 + 1):
    dp[i][0] = i

for j in range(l2 + 1):
    dp[0][j] = j

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(
                dp[i - 1][j - 1] + 1,
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1
            )

print(dp[l1][l2])





