from collections import deque

def topological_sort(n, adj, in_degree):
    """Perform topological sort and return the valid ordering if possible"""
    queue = deque()
    result = []
    
    # Start with nodes having no incoming edges (in_degree == 0)
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Decrease the in-degree of adjacent nodes
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we have a valid topological order, return it
    if len(result) == n:
        return result
    else:
        return None  # Cycle detected, so no valid topological ordering

def trotter_johnson_rank_recursive(perm):
    """
    Calculates the rank of perm for numbers {1,..,len(perm)} for the Trotter-Johnson order recursively
    """
    rank = 0
    n = len(perm)
    if n > 1:
        k = 0
        while perm[k] != n:
            k += 1  # We find where n is in the permutation
        high_perm = []
        if k < n - 1:
            high_perm = perm[k + 1:]
        rec_perm = perm[:k] + high_perm  # The numbers at the right of n will be moved one place to the left
        rec_rank = trotter_johnson_rank_recursive(rec_perm)  # Recursively calculate the rank of the new permutation
        if rec_rank % 2:  # According to whether the recursive permutation was odd or even
            rank = n * rec_rank + k
        else:
            rank = n * rec_rank + (n - 1 - k)
    return rank

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    precedence_pairs = []

    # Reading precedence pairs
    for _ in range(m):
        a, b = map(int, input().split())
        precedence_pairs.append((a, b))

    # Step 1: Build the graph and compute the in-degree of each node
    in_degree = [0] * (n + 1)
    for a, b in precedence_pairs:
        adj[a].append(b)
        in_degree[b] += 1
    
    # Step 2: Perform topological sort
    valid_ordering = topological_sort(n, adj, in_degree)
    
    if not valid_ordering:
        print("Impossible to satisfy the conditions")  # No valid permutation exists
    else:
        # Step 3: Calculate the rank of the valid permutation in Trotter-Johnson ordering
        rank = trotter_johnson_rank_recursive(valid_ordering)
        print(rank)

if __name__ == "__main__":
    main()
