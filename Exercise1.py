''' import math '''

'''
#The function to compute combinatorial number
def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)  

#Here's the code from the book
def k_subset_lex_rank(T: list, k: int, n: int) -> int:
    r = 0           
    t_prev = 0      

    for i in range(k):  
        if t_prev + 1 <= T[i] - 1:
            for j in range(t_prev + 1, T[i]):
                r += binomial(n - j, k - i - 1)
        t_prev = T[i]
    return r
'''
# Checks whether two vertices are neighbors
# Here's the code from the class
def are_neighbors_l(v:int, w:int)->bool:
    return (w in G_l[v])

# The function to count edges between two vertices 
def count_edges(nodes:list) -> int:
    count = 0
    for i in range(4):
        for j in range(i + 1,4):
            if are_neighbors_l(nodes[i],nodes[j]):
                count = count + 1
    return count

# The function to justify if nodes are form of paw
def is_paw(nodes:list) -> bool:
    #Find all the combination of triangle
    for i in range(4):
        tri = []
        for j in range(4):
            if j != i:
                tri.append(nodes[j]) 
        a_vertex = nodes[i]
        # Checks if tri is triangle
        if are_neighbors_l(tri[0],tri[1]) and are_neighbors_l(tri[0],tri[2]) and are_neighbors_l(tri[1],tri[2]):
            # Checks if a_vertex connects only one vertex of triangle
            count = 0
            for elem in tri:
                if are_neighbors_l(elem,a_vertex):
                    count = count + 1
            if count == 1:
                return True
    return False                        
                    

# Read the input
line = input()            # input 7 10 -> "7 10"           
parts = line.split()      # "7 10".split() -> ["7", "10"] 
n = int(parts[0])         # n = int("7") = 7
m = int(parts[1])         # m = int("10") = 10

# Adjacency List Representation
# Initialization
G_l = []
for i in range(n):
    G_l.append([])
    
# Adding all the edges
for i in range(m):
    edge_line = input()            # input 1 2 -> "1 2"
    edge_parts = edge_line.split() # "1 2".split() -> ["1", "2"]
    v = int(edge_parts[0])         # v = int("1") = 1
    w = int(edge_parts[1])         # w = int("2") = 2
    G_l[v].append(w)
    G_l[w].append(v)

# Generating all possible cases of nodes which are paw
paws = []
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            for d in range(c + 1, n):
                nodes = [a, b, c, d]
                if count_edges(nodes) == 4:
                    if is_paw(nodes):
                        paws.append(nodes)

# Printing out the result
if len(paws) == 0:
    print("It found no paws in the graph.")
else:
    for p in paws:
        print(p)
        
'''
# Ranking the elements of paws with lexicographic order
ranked_paws = []

for paw in paws:
    rank = k_subset_lex_rank(paw, 4, n)  # The lexicographic order of every paw in paws
    ranked_paws.append((rank, paw))      # Pairwise ranking and paw

# Tuple in rank order
ranked_paws.sort()

# Printing out all the paw
for rank, paw in ranked_paws:
    print(paw)
'''
