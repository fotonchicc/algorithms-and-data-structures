import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

included = [False] * n

min_dist = [float('inf')] * n
min_dist[0] = 0

p_q = [(0, 0)]

total_weight = 0

while p_q:
    dist, ver = heapq.heappop(p_q)

    if included[ver]:
        continue

    total_weight += dist

    included[ver] = True

    for v, weight in graph[ver]:
        if not included[v] and weight < min_dist[v]:
            min_dist[v] = weight
            heapq.heappush(p_q, (weight, v))

print(total_weight)
