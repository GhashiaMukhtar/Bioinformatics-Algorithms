def BuildProfileWithPseudocounts(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)

    profile = {'A': [1.0]*k, 'C': [1.0]*k, 'G': [1.0]*k, 'T': [1.0]*k}
    
    for i in range(k):
        for motif in Motifs:
            profile[motif[i]][i] += 1.0

    for nucleotide in "ACGT":
        for i in range(k):
            profile[nucleotide][i] = profile[nucleotide][i] / (t + 4.0)
            
    return profile
