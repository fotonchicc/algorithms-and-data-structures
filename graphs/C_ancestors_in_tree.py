import sys

data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
n, m = data[0]
ancestors = data[1]
requests = data[2:]

graph = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    ancestor = ancestors[i - 2]
    graph[ancestor].append(i)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
timer = [0]

def dfs(v):
    stack = [v]
    while stack:
        node = stack[-1]
        if tin[node] == 0:
            timer[0] += 1
            tin[node] = timer[0]
            visited = False
            for child in graph[node]:
                if tin[child] == 0:
                    stack.append(child)
                    visited = True
            if not visited:
                stack.pop()
                timer[0] += 1
                tout[node] = timer[0]
        else:
            stack.pop()
            timer[0] += 1
            tout[node] = timer[0]
dfs(1)

response = []

for u, v in requests:
    if tin[u] <= tin[v] and tout[u] >= tout[v]:
        response.append('1')
    else:
        response.append('0')

sys.stdout.write("\n".join(map(str, response)))
