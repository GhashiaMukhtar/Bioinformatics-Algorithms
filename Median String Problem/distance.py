def hamming_distance(seq1, seq2):
    mismatches = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mismatches += 1
    return mismatches

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    total_distance = 0
    
    for string in Dna:
        min_hamming_dist = float("inf")
        for i in range(len(string) - k + 1):
            k_mer = string[i:i+k]
            k_dist = hamming_distance(Pattern, k_mer)

            if min_hamming_dist > k_dist:
                min_hamming_dist = k_dist

        total_distance += min_hamming_dist

    return total_distance
