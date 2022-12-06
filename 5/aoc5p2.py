import re
crates = []
movesList = []
input = [l.strip("\n") for l in open("input").readlines()]
index = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : []}
crates = input[:8]
moves = input[10:]

for crate in crates:
    for i, char in enumerate(crate):
        if char.isupper():
            index[i//4+1] = [char] + index[i//4+1]

for line in moves:
    movesList.append([s for s in re.findall(r'-?\d+\.?\d*', line)])

for move in movesList:
    for val in range (0, int((move[0]))):
        index[int(move[2])].extend((index[int(move[1])][-(int((move[0]))):]))
        del index[int(move[1])][-(int((move[0]))):]
        break

message = ""
for i in index:
   message += (index[i][-1])

print("Message: " + message)
