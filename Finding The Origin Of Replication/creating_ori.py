from calculate_skew import minimum_skew

path = "Salmonella_enterica.txt"
with open(path) as f:
    name = f.readline()
    genome = f.read().replace("\n","")

minimum_val, minimum_postion = minimum_skew(genome)


ori = ""
for position in minimum_postion:
    start = max(0, position - 250)
    end = min(len(genome), position + 250)
    window = genome[start:end]
    ori += window

with open("possible_ori.txt", "w") as f:
    f.write(ori)
