from 4K_DNACombinations import AllStrings
from distance import DistanceBetweenPatternAndStrings
def MedianString(Dna, k):
    best_distance = float("inf")
    Median = ""
    
    patterns = AllStrings(k)
    
    for pattern in patterns:
        current_dist = DistanceBetweenPatternAndStrings(pattern, Dna)

        if best_distance > current_dist:
            best_distance = current_dist
            Median = pattern

    return Median
