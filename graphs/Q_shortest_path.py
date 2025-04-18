import heapq
import sys

n, s, f = map(int, sys.stdin.readline().split())
s -= 1
f -= 1

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def dijkstra(graph, start, finish):
    dist = [float('inf')] * n
    dist[start] = 0
    p_q = [(0, start)]

    while p_q:
        cur_dist, v = heapq.heappop(p_q)

        if cur_dist > dist[v]:
            continue

        for u, weight in enumerate(graph[v]):
            if weight == -1:
                continue

            new_dist = cur_dist + weight
            if new_dist < dist[u]:
                dist[u] = new_dist
                heapq.heappush(p_q, (new_dist, u))

    return dist[finish] if dist[finish] != float('inf') else -1


res = dijkstra(graph, s, f)
print(res)
