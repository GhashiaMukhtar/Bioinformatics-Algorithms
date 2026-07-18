def AllStrings(k):
    """Recursively generates all 4^k possible DNA combinations."""
    if k == 1:
        return ["A", "C", "G", "T"]

    prefixes = AllStrings(k - 1)
    result = []
    for prefix in prefixes:
        for nucleotide in ["A", "C", "G", "T"]:
            result.append(prefix + nucleotide)
    return result
