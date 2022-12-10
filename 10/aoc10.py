input = [l.strip("\n") for l in open("input").readlines()]

for idx, line in enumerate(input):  
    input[idx] = line.split()

def checkCycle(cycle, i):
    if (cycle == 20) | (cycle == 60) | (cycle == 100) | (cycle == 140) | (cycle == 180) | (cycle == 220):
        return (i * cycle)
    else:
        return 0


def getCycles():
    sum = 0   
    cycle = 1
    i = 1      
    
    for line in input:
        if line[0] == "addx":
            sum += checkCycle(cycle, i)
            cycle += 1

            sum += checkCycle(cycle, i)
            i += (int(line[1]))
            cycle += 1

        else:
            sum += checkCycle(cycle, i)
            cycle += 1
           
    return sum




print(getCycles())