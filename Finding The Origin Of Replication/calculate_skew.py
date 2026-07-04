def minimum_skew(genome):
    skew = [0]
    count = 0
    for i in range(len(genome)):
        if genome[i]=="C":
            count -=1
        elif genome[i]=="G":
            count +=1
        skew.append(count)


    minimum_val = min(skew)
    minimum_position = []
    for i in range(len(skew)):
        if skew[i] == minimum_val:
            minimum_position.append(i)

    return minimum_val, minimum_position
if __name__ == "__main__":
    path = "Salmonella_enterica.txt"
    with open(path) as f:
        name = f.readline()
        genome = f.read().replace("\n","")

    minimum_val, minimum_postion = minimum_skew(genome)

    print(f"minimum value:{minimum_val}\nminimum position:{minimum_postion}")