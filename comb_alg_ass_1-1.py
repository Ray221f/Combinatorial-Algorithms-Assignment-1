# Read the input: n, the number of the vertices; m, the number of edges
# .split() splits the input string into the list of nuymbers based on spaces
# map fucntion concerts the string into numbers
n, m = map(int, input().split())

# If the number of vertices less than 4, meaning no paws, then exit
if n < 4:
    print("No paws found in the graph")
    exit()

# Build adjacency sets
adj = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

# Initialize the result, where result = the set of all possible paws
result = []

# Generate all 4-node combinations
# In lexicographic oder
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

                # If #edges != 4, then it fail in forming a paw
                # 'continue' function means skip the remaining codes for determing the structure of the paw
                if edges != 4:
                    continue

                # Check each possible triplet for triangle and fourth node
                # cnt = the number of edges between the fourth node and the nodes forming the triangle
                
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

