import sys
from sys import setrecursionlimit
import threading
setrecursionlimit(2 * 10 ** 5)
threading.stack_size(67108864)


def main():
    data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
    n, m = data[0]
    edges = data[1:]

    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n + 1)
    cur_color = 0

    def dfs(v, color):
        colors[v] = color
        for neighbor in graph[v]:
            if colors[neighbor] == 0:
                dfs(neighbor, color)

    for i in range(1, n + 1):
        if colors[i] == 0:
            cur_color += 1
            dfs(i, cur_color)

    print(" ".join(map(str, colors[1:])))


thread = threading.Thread(target=main)
thread.start()



