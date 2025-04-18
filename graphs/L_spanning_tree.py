import math
import sys

def main():
    n = int(sys.stdin.readline())
    vertex_coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    inf = float('inf')
    included = [False] * n
    min_distance = [inf] * n
    min_distance[0] = 0
    total_weight = 0

    for _ in range(n):
        ver = -inf
        for i in range(n):
            if not included[i] and (ver == -inf or min_distance[i] < min_distance[ver]):
                ver = i

        included[ver] = True
        total_weight += min_distance[ver]

        for v in range(n):
            if not included[v]:
                dx = vertex_coordinates[ver][0] - vertex_coordinates[v][0]
                dy = vertex_coordinates[ver][1] - vertex_coordinates[v][1]
                dist = math.sqrt(dx * dx + dy * dy)
                if dist < min_distance[v]:
                    min_distance[v] = dist

    print(f"{total_weight:.10f}")

if __name__ == "__main__":
    main()
