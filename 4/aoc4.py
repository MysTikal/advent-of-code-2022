splitlines = []
result = []
finallist = []
count = 0

with open('input') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    line = line.split(",")
    for splitline in line:
        splitline = splitline.split("-")
        splitlines.append(splitline)

splitlines = list(zip(splitlines,splitlines[1:]))[::2]

def complete(input):
    pair1 = []
    pair2 = []
    result = []

    for val in range (int(input[0][0]), int(input[0][1])+1):
        pair1.append(val)

    for val in range (int(input[1][0]), int(input[1][1])+1):
        pair2.append(val)

    result.append(pair1) 
    result.append(pair2) 
    return result

for i in range(0,len(lines)):
    finallist.append(complete(splitlines[i]))

print(finallist)

for pair in finallist:
    g0 = set(pair[0])
    g1 = set(pair[1])

    # if subset
    # if (g0.issubset(g1)) | (g1.issubset(g0)):
    #     count += 1

    if (g0 & g1): #if intersection
        count+= 1

print(count)
