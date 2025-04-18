import sys

n, m, k, s = map(int, sys.stdin.readline().split())
s -= 1

edges = []

for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    edges.append((a, b, w))

dist = [[float('inf')] * n for _ in range(k + 1)]
dist[0][s] = 0

for i in range(1, k + 1):
    for a, b, w in edges:
        if dist[i - 1][a] != float('inf'):
            dist[i][b] = min(dist[i][b], dist[i - 1][a] + w)

for i in range(n):
    if dist[k][i] == float('inf'):
        print(-1)
    else:
        print(dist[k][i])
        