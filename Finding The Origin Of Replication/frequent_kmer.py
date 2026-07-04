def reverse_complement(seq):
    """Standard RC helper function."""
    mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join([mapping[base] for base in seq])[::-1]

def generate_neighbors(pattern, d):
    """Generates d-mismatch neighbors (standard forward only)."""
    neighborhood = {pattern}
    nucleotides = ['A', 'C', 'G', 'T']
    
    for _ in range(d):
        new_neighbors = set()
        for seq in neighborhood:
            for i in range(len(seq)):
                for base in nucleotides:
                    new_neighbors.add(seq[:i] + base + seq[i+1:])
        neighborhood.update(new_neighbors)
        
    return list(neighborhood)

def frequent_words_with_mismatches_and_rc(text, k, d):
    """The complete algorithm for double-stranded DNA."""
    freq_map = {}
    
    # 1. Slide the window and build the standard mismatch ballot box
    for i in range(len(text) - k + 1):
        window = text[i : i+k]
        neighbors = generate_neighbors(window, d)
        
        for neighbor in neighbors:
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1
                
    # 2. The Grand Tally: Combine votes for both strands
    total_scores = {}
    
    # We only need to check sequences that received at least one vote
    for pattern in freq_map.keys():
        rc_pattern = reverse_complement(pattern)
        
        # Score = Forward Votes + Reverse Strand Votes
        # We use .get(key, 0) just in case the reverse complement got 0 votes
        forward_votes = freq_map.get(pattern, 0)
        reverse_votes = freq_map.get(rc_pattern, 0)
        
        total_scores[pattern] = forward_votes + reverse_votes
        
    # 3. Find the absolute maximum score
    max_score = max(total_scores.values())
    
    # 4. Collect the winners
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