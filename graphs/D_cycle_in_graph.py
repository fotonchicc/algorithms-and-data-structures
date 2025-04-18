import sys
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

    visited = [False] * (n + 1)
    stack = [False] * (n + 1)
    parent = [-1] * (n + 1)

    def dfs(v):
        visited[v] = True
        stack[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                parent[neighbor] = v
                if dfs(neighbor):
                    return True
            elif stack[neighbor]:
                cycle_path = []
                cur = v
                while cur != neighbor:
                    cycle_path.append(cur)
                    cur = parent[cur]
                cycle_path.append(neighbor)
                cycle_path.reverse()
                print(f"{len(cycle_path)}\n{' '.join(map(str, cycle_path))}")
                return True

        stack[v] = False
        return False

    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i):
                return
    print(-1)


thread = threading.Thread(target=main)
thread.start()
