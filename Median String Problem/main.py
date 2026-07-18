from MedianString import MedianString
path = input("Enter file path: ")
with open(path) as f:
    k = int(f.readline().strip())
    
    Dna = f.read().strip().upper().split()

print(MedianString(Dna, k))
