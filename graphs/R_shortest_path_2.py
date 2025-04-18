import heapq
import sys

data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())
edges_data = [tuple(map(int, line.split())) for line in data[1:]]

graph = [[] for _ in range(n + 1)]
for u, v, w in edges_data:
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    p_q = [(0, start)]

    while p_q:
        cur_dist, current_vertex = heapq.heappop(p_q)

        if cur_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = cur_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(p_q, (distance, neighbor))

    return distances

distances = dijkstra(1)

print(' '.join(map(str, distances[1:])))
