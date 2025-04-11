import sys
import heapq

def topological_sort(n, edges):
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for a, b in edges:
        adj[a].append(b)
        in_degree[b] += 1

    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    topo_order = []
    while heap:
        u = heapq.heappop(heap)
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    return topo_order if len(topo_order) == n else None

def trotter_johnson_rank(perm):
    rank = 0
    n = len(perm)
    for i in range(n):
        k = perm[i]
        left = perm[:i]
        smaller = sum(1 for x in left if x < k)
        if i % 2 == 1:
            smaller = k - 1 - smaller
        rank = rank * (i + 1) + smaller
    return rank

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    m = int(input[ptr + 1])
    ptr += 2
    edges = []
    for _ in range(m):
        a = int(input[ptr])
        b = int(input[ptr + 1])
        edges.append((a, b))
        ptr += 2

    topo_order = topological_sort(n, edges)
    if not topo_order:
        print("impossible")
    else:
        print(trotter_johnson_rank(topo_order))

if __name__ == "__main__":
    main()