from ProbableKmer import ProfileMostProbableKmer
from Score import Score
from Profile import BuildProfileWithPseudocounts
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for string in Dna:
        BestMotifs.append(string[0:k])
        
    best_score = Score(BestMotifs)
    first_string = Dna[0]
    
    for i in range(len(first_string) - k + 1):
        anchor_motif = first_string[i:i+k]
        current_motifs = [anchor_motif]
        
        for j in range(1, t):
            current_profile = BuildProfileWithPseudocounts(current_motifs)
            next_best_motif = ProfileMostProbableKmer(Dna[j], k, current_profile)
            current_motifs.append(next_best_motif)
            
        current_score = Score(current_motifs)
        if current_score < best_score:
            best_score = current_score
            BestMotifs = current_motifs
            
    return BestMotifs


def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for string in Dna:
        BestMotifs.append(string[0:k])
        
    best_score = Score(BestMotifs)

    first_string = Dna[0]
    for i in range(len(first_string) - k + 1):
        anchor_motif = first_string[i:i+k]

        current_motifs = [anchor_motif]

        for j in range(1, t):
            current_profile = BuildProfile(current_motifs)
            
            next_best_motif = ProfileMostProbableKmer(Dna[j], k, current_profile)

            current_motifs.append(next_best_motif)

        current_score = Score(current_motifs)
        if current_score < best_score:
            best_score = current_score
            BestMotifs = current_motifs
            
    return BestMotifs
