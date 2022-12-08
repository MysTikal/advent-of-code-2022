input = [l.strip("\n") for l in open("input").readlines()]

trees = []
total = 0

for idx, line in enumerate(input):
    trees.append([*line])

def isVisible(x,y):
    uCount = 0
    dCount = 0
    lCount = 0
    rCount = 0
    i = y+1
    while i < len(trees[0]): #right
        i += 1
        if trees[x][y] > trees[x][i-1]:
            rCount += 1
        if trees[x][y] <= trees[x][i-1]:
            rCount += 1
            break                
    i = y+1
    while i > 1: #left
        i -= 1
        if trees[x][y] > trees[x][i-1]:
                lCount += 1
        if trees[x][y] <= trees[x][i-1]:
                lCount += 1
                break
    i = x+1
    while i < len(trees): # down
        i += 1
        if trees[x][y] > trees[i-1][y]:
            dCount += 1
        if trees[x][y] <= trees[i-1][y]:
            dCount += 1
            break
    i = x+1
    while i > 1: #up
        i -= 1
        if trees[x][y] > trees[i-1][y]:
            uCount += 1
        if trees[x][y] <= trees[i-1][y]:
            uCount += 1
            break
    total = uCount * lCount * rCount * dCount
    return (total)


scoreCount = []
for x, line in enumerate(trees):
    for y, char in enumerate(line):
        scoreCount.append(isVisible(x,y))

print(max(scoreCount))

