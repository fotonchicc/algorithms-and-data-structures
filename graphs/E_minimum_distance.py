import sys
from collections import deque
from sys import setrecursionlimit
import threading

setrecursionlimit(2 * 10 ** 6)
threading.stack_size(67108864)


def main():
    data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
    n, m = data[0]
    edges = data[1:]
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)
    dist[1] = 0

    queue = deque([1])
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[v] + 1
                queue.append(neighbor)

    print(" ".join(map(str, dist[1:])))


thread = threading.Thread(target=main)
thread.start()
