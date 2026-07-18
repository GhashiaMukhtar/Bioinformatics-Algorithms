from MotifEnumeration import MotifEnumeration
path = input("Enter file path: ")
with open(path) as f:
    first_line = f.readline().strip().split()
    k = int(first_line[0])
    d = int(first_line[1])
    
    text = f.read().split()

result = MotifEnumeration(text, k, d)

with open("motif.txt", "w") as f:
    f.write(" ".join(result))
    
print("Success! Check motif.txt for your results.")
