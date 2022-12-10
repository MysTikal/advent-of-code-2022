input = [l.strip("\n") for l in open("input").readlines()]

for idx, line in enumerate(input):  
    input[idx] = line.split()

finalList = []

def checkCycle(cycle, i):
    if abs((cycle-1)%40 - i) < 2:
        finalList.append("#")
    else:
        finalList.append(".")

def getCycles():
    cycle = 1
    i = 1      
    
    for line in input:
        if line[0] == "addx":
            checkCycle(cycle, i)
            cycle += 1

            checkCycle(cycle, i)
            i += (int(line[1]))
            cycle += 1
            
        else:
            checkCycle(cycle, i)
            cycle += 1

(getCycles())
print(*finalList)