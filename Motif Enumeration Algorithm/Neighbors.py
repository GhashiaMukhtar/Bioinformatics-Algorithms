def Neighbors(pattern, d):
    """Generates all k-mers that differ from the pattern by at most d mismatches."""
    if d == 0:
        return {pattern}
    if len(pattern) == 0:
        return {""}
    
    nucleotides = ['A', 'C', 'G', 'T']
    neighborhood = set()
    

    suffix_neighbors = Neighbors(pattern[1:], d)
    
    for text in suffix_neighbors:
        if HammingDistance(pattern[1:], text) == d:
            neighborhood.add(pattern[0] + text)
        else:
            for n in nucleotides:
                neighborhood.add(n + text)
                
    return neighborhood
