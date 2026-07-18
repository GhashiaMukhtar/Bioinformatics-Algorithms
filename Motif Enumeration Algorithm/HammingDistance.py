def HammingDistance(p, q):
    """Calculates the number of mismatches between two strings of equal length."""
    mismatches = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatches += 1
    return mismatches
