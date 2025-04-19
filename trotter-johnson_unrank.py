import math

def trotter_johnson_unrank_recursive(n: int, r: int) -> list:
    """
    Calculates the permutation of {1,..,n} for rank r on the Trotter-Johnson order recursively
    """
    perm = [1]
    if n > 1:
        rec_rank = math.floor(r / n)
        rec_perm = trotter_johnson_unrank_recursive(n - 1, rec_rank)  # Get the rank for the (n-1) permutation
        k = r - n * rec_rank
        if not rec_rank % 2:  # We add n in the correct place
            perm = rec_perm[:n - 1 - k] + [n] + rec_perm[n - 1 - k:]
        else:
            perm = rec_perm[:k] + [n] + rec_perm[k:]
    return perm

def main():
    # Taking user input for n and r
    n = int(input("Enter the value of n (size of the set): "))
    r = int(input("Enter the rank r: "))
    
    # Calculate the permutation
    permutation = trotter_johnson_unrank_recursive(n, r)
    
    # Output the result
    print(f"The permutation of size {n} for rank {r} is: {permutation}")

if __name__ == "__main__":
    main()
