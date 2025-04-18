import sys

data = [list(map(lambda x: int(x), a.split())) for a in sys.stdin.read().splitlines()]
n, m = data[0]
edges = data[1:]
print(n)

output = {}
for values in edges:
    top_out = values[0]
    top_in = values[1]
    if top_out in output:
        output[top_out][1].append(top_in)
    else:
        output[top_out] = [0, [top_in]]
    output[top_out][0] += 1

for i in range(1, n + 1):
    if i not in output:
        print(0)
    else:
        out_edges = output.get(i)[1]
        out_edges.sort()
        print(output.get(i)[0], *out_edges)

