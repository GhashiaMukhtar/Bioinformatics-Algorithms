def reverse_complement(seq):
    """Standard RC helper function."""
    mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join([mapping[base] for base in seq])[::-1]

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

def frequent_words_with_mismatches_and_rc(text, k, d):
    """The complete algorithm for double-stranded DNA."""
    freq_map = {}

    for i in range(len(text) - k + 1):
        window = text[i : i+k]
        neighbors = generate_neighbors(window, d)
        
        for neighbor in neighbors:
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1

    total_scores = {}
    for pattern in freq_map.keys():
        rc_pattern = reverse_complement(pattern)
        
        forward_votes = freq_map.get(pattern, 0)
        reverse_votes = freq_map.get(rc_pattern, 0)
        
        total_scores[pattern] = forward_votes + reverse_votes

    max_score = max(total_scores.values())

    winners = []
    for pattern, score in total_scores.items():
        if score == max_score:
            winners.append(pattern)
            
    return winners


path = "possible_ori.txt"
with open(path) as f:
    seq = f.readline().strip()

result = frequent_words_with_mismatches_and_rc(seq, 9, 1)
print(f"The most frequent kmer with one mismatch and reverse complments are:\n{result}")
