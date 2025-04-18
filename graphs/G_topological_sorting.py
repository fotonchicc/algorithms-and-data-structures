import sys
from sys import setrecursionlimit
import threading

setrecursionlimit(100_000)
threading.stack_size(67108864)


def main():
    data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
    n, m = data[0]
    edges = data[1:]
    graph = [[] for _ in range(n + 1)]

    for a, b in edges:
        graph[a].append(b)

    visited = [False] * (n + 1)
    cycle_stack = [False] * (n + 1)
    stack = []
    is_possible = True

    def dfs(v):
        nonlocal is_possible
        if not is_possible:
            return
        visited[v] = True
        cycle_stack[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
            elif cycle_stack[neighbor]:
                is_possible = False
                return
        cycle_stack[v] = False
        stack.append(v)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
        if not is_possible:
            break

    if is_possible:
        stack.reverse()
        print(*stack)
    else:
        print(-1)


thread = threading.Thread(target=main)
thread.start()
