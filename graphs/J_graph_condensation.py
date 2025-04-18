import sys
from sys import setrecursionlimit
import threading

setrecursionlimit(10_000)
threading.stack_size(67108864)


def main():
    data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
    n, m = data[0]
    edges = data[1:]
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for b, e in edges:
        graph[b].append(e)
        reverse_graph[e].append(b)

    visited = [False] * (n + 1)
    final_order = []

    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        final_order.append(v)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    component = [-1] * (n + 1)
    component_number = 0

    def dfs_comp(v, component_num):
        component[v] = component_num
        for neighbor in reverse_graph[v]:
            if component[neighbor] == -1:
                dfs_comp(neighbor, component_num)

    for j in reversed(final_order):
        if component[j] == -1:
            component_number += 1
            dfs_comp(j, component_number)

    condensation_edges = set()
    for b, e in edges:
        c_b, c_e = component[b], component[e]
        if c_b != c_e:
            condensation_edges.add((c_b, c_e))

    print(len(condensation_edges))


thread = threading.Thread(target=main)
thread.start()
