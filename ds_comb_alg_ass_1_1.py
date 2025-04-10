n, m = map(int, input().split())

if n < 4:
    print("No paws found in the graph")
    exit()

# Build adjacency sets
adj = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

result = []

# Generate all 4-node combinations
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                # Count edges in the subset
                edges = 0
                edges += 1 if j in adj[i] else 0
                edges += 1 if k in adj[i] else 0
                edges += 1 if l in adj[i] else 0
                edges += 1 if k in adj[j] else 0
                edges += 1 if l in adj[j] else 0
                edges += 1 if l in adj[k] else 0

                if edges != 4:
                    continue

                # Check each possible triplet for triangle and fourth node
                # Triplet 1: i, j, k; fourth is l
                if (j in adj[i]) and (k in adj[i]) and (k in adj[j]):
                    cnt = 0
                    cnt += 1 if l in adj[i] else 0
                    cnt += 1 if l in adj[j] else 0
                    cnt += 1 if l in adj[k] else 0
                    if cnt == 1:
                        result.append([i, j, k, l])
                        continue

                # Triplet 2: i, j, l; fourth is k
                if (j in adj[i]) and (l in adj[i]) and (l in adj[j]):
                    cnt = 0
                    cnt += 1 if k in adj[i] else 0
                    cnt += 1 if k in adj[j] else 0
                    cnt += 1 if k in adj[l] else 0
                    if cnt == 1:
                        result.append([i, j, k, l])
                        continue

                # Triplet 3: i, k, l; fourth is j
                if (k in adj[i]) and (l in adj[i]) and (l in adj[k]):
                    cnt = 0
                    cnt += 1 if j in adj[i] else 0
                    cnt += 1 if j in adj[k] else 0
                    cnt += 1 if j in adj[l] else 0
                    if cnt == 1:
                        result.append([i, j, k, l])
                        continue

                # Triplet 4: j, k, l; fourth is i
                if (k in adj[j]) and (l in adj[j]) and (l in adj[k]):
                    cnt = 0
                    cnt += 1 if i in adj[j] else 0
                    cnt += 1 if i in adj[k] else 0
                    cnt += 1 if i in adj[l] else 0
                    if cnt == 1:
                        result.append([i, j, k, l])
                        continue

if not result:
    print("No paws found in the graph")
else:
    for subset in result:
        print(subset)