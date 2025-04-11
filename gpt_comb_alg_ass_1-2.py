from collections import deque, defaultdict

def topological_sort(n, m, constraints):
    # Graph initialization
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    # Building the graph based on the constraints
    for a, b in constraints:
        graph[a].append(b)
        in_degree[b] += 1

    # Kahn's algorithm: finding the topological sort
    queue = deque()
    
    # Start with all nodes that have no incoming edges (in_degree 0)
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        current = queue.popleft()
        result.append(current)

        # Process all nodes that current points to
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we have processed all nodes, return the result (permutation)
    if len(result) == n:
        return result
    else:
        # If there's a cycle, it's impossible to satisfy the constraints
        return "Impossible"

# Read input
n, m = map(int, input().split())
constraints = [tuple(map(int, input().split())) for _ in range(m)]

# Get the topological order
result = topological_sort(n, m, constraints)

# Print the result
if result == "Impossible":
    print("Impossible")
else:
    # Print the permutation
    print(" ".join(map(str, result)))
