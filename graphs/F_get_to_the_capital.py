import sys
from collections import deque
from sys import setrecursionlimit
import threading

setrecursionlimit(2 * 10 ** 5)
threading.stack_size(67108864)


def main():
    data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
    n, s, m = data[0]
    edges = data[1:]
    graph = [[] for _ in range(n + 1)]

    for a, b in edges:
        graph[b].append(a)

    dist = [-1] * (n + 1)
    dist[s] = 0

    queue = deque([s])
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[v] + 1
                queue.append(neighbor)

    print(" ".join(map(str, dist[1:])))


thread = threading.Thread(target=main)
thread.start()
