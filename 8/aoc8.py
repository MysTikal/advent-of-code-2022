input = [l.strip("\n") for l in open("input").readlines()]

trees = []
total = 0

for idx, line in enumerate(input):
    trees.append([*line])

def isVisible(x,y):
    if y == len(trees[0])-1:
        return True
    elif y == 0:
        return True
    elif x == len(trees)-1:
        return True
    elif x == 0:
        return True
    else: 
        visibleR = True
        visibleL = True
        visibleU = True
        visibleD = True
        count = 0
        i = y+1
        while i < len(trees[0]): # right
            i += 1
            if trees[x][y] <= trees[x][i-1]:
                visibleR = False
            else:
                count += 1
        i = y+1
        while i > 1: # left
            i -= 1
            if trees[x][y] <= trees[x][i-1]:
                visibleL = False
        i = x+1
        while i < len(trees): # down
            i += 1
            if trees[x][y] <= trees[i-1][y]:
                visibleD = False
        i = x+1
        while i > 1:  # up
            i -= 1
            if trees[x][y] <= trees[i-1][y]:
                visibleU = False
        return any([visibleU, visibleD, visibleL, visibleR])

for x, line in enumerate(trees):
    for y, char in enumerate(line):
        if isVisible(x,y):
            total += 1

print(total)

