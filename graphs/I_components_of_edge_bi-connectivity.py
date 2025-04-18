import sys
from sys import setrecursionlimit
import threading

setrecursionlimit(20_000)
threading.stack_size(67108864)


def main():
    data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
    n, m = data[0]
    edges = data[1:]
    graph = [[] for _ in range(n + 1)]

    for index, (b, e) in enumerate(edges):
        graph[b].append((e, index))
        graph[e].append((b, index))

    tin = [-1] * (n + 1)
    f = [-1] * (n + 1)
    visited = [False] * (n + 1)
    bridges = []
    timer = [0]
    component = [-1] * (n + 1)
    component_number = 0

    def dfs(v, p):
        visited[v] = True
        tin[v] = f[v] = timer[0]
        timer[0] += 1
        for neighbor, inx in graph[v]:
            if neighbor == p:
                continue
            if visited[neighbor]:
                f[v] = min(f[v], tin[neighbor])
            else:
                dfs(neighbor, v)
                f[v] = min(f[v], f[neighbor])

                if f[neighbor] > tin[v]:
                    bridges.append(inx)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)

    def assign_components(v, component_num):
        stack = [v]
        component[v] = component_num
        while stack:
            node = stack.pop()
            for neighbor, idx in graph[node]:
                if component[neighbor] == -1 and idx not in bridges:
                    component[neighbor] = component_num
                    stack.append(neighbor)

    for i in range(1, n + 1):
        if component[i] == -1:
            component_number += 1
            assign_components(i, component_number)

    print(component_number)
    print(" ".join(map(str, component[1:])))


thread = threading.Thread(target=main)
thread.start()
