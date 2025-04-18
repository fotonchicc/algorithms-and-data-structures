import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
prev = [-1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

max_inx  = dp.index(max(dp))

subsequence = []

while max_inx != -1:
    subsequence.append(a[max_inx])
    max_inx = prev[max_inx]

subsequence.reverse()

print(max(dp))
print(*subsequence)
