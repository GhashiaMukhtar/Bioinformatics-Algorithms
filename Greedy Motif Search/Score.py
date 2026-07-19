def Score(Motifs):
    score = 0
    k = len(Motifs[0])
    t = len(Motifs)
    for i in range(k):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in Motifs:
            counts[motif[i]] += 1
        max_count = max(counts.values())
        score += (t - max_count)
    return score
