def MotifEnumeration(Dna, k, d):
    """
    Finds all (k, d)-motifs in a collection of strings.
    """
    Patterns = set()
    
    first_string = Dna[0]
    
    for i in range(len(first_string) - k + 1):
        kmer = first_string[i:i+k]
        
        neighborhood = Neighbors(kmer, d)
        
        for candidate in neighborhood:
            appears_in_all = True

            for dna_string in Dna:
                found_in_this_string = False

                for j in range(len(dna_string) - k + 1):
                    current_kmer = dna_string[j:j+k]
                    if HammingDistance(candidate, current_kmer) <= d:
                        found_in_this_string = True
                        break
                
                if not found_in_this_string:
                    appears_in_all = False
                    break 

            if appears_in_all:
                Patterns.add(candidate)

    return set(Patterns)
