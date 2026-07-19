def ProfileMostProbableKmer(string, k, profile):
    best_prob = -1.0 
    best_kmer = string[0:k]
    
    for i in range(len(string) - k + 1):
        kmer = string[i:i+k]
        calculation = 1.0
        for j in range(k):
            symbol = kmer[j]
            calculation = calculation * profile[symbol][j]
            
        if calculation > best_prob:
            best_prob = calculation
            best_kmer = kmer
            
    return best_kmer
