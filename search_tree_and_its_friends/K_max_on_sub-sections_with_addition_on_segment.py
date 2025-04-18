import sys

class Vertex:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def apply(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, node, start, end, l, r, val):
        self.apply(node, start, end)

        if r < start or end < l:
            return

        if l <= start and end <= r:
            self.lazy[node] += val
            self.apply(node, start, end)
            return

        mid = (start + end) // 2
        self.update_range(2 * node + 1, start, mid, l, r, val)
        self.update_range(2 * node + 2, mid + 1, end, l, r, val)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query_range(self, node, start, end, l, r):
        self.apply(node, start, end)

        if r < start or end < l:
            return -float('inf')

        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_query = self.query_range(2 * node + 1, start, mid, l, r)
        right_query = self.query_range(2 * node + 2, mid + 1, end, l, r)

        return max(left_query, right_query)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])


def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    m = int(data[2])
    queries = data[3:]

    seg_tree = Vertex(n)
    seg_tree.build(arr, 0, 0, n - 1)

    result = []

    for query in queries:
        parts = query.split()
        if parts[0] == 'm':
            l, r = int(parts[1]) - 1, int(parts[2]) - 1
            res = seg_tree.query_range(0, 0, n - 1, l, r)
            result.append(res)
        elif parts[0] == 'a':
            l, r, add = int(parts[1]) - 1, int(parts[2]) - 1, int(parts[3])
            seg_tree.update_range(0, 0, n - 1, l, r, add)

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
