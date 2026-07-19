from GreedyMotif import GreedyMotifSearchWithPseudocounts
path = input("Enter file path: ")
with open(path) as f:
    first_line = f.readline().strip().split()
    k = int(first_line[0])
    t = int(first_line[1])
    Dna = f.read().strip().upper().split()

winners = GreedyMotifSearchWithPseudocounts(Dna, k, t)

for motif in winners:
    print(motif)
