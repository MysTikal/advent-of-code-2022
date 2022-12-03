with open('input') as file:
    lines = [line.rstrip() for line in file]

groupMatches = []
badges = []
badgesGroup = []
grouped = list(zip(*(iter(lines),) * 3))

for group in grouped: 
    for char in group[0]:
        if char in group[1]:
            groupMatches.append(char)

    for char in group[2]:
        if char in groupMatches and char not in badgesGroup:
            badges.append(char)
            badgesGroup.append(char)
    groupMatches.clear()
    badgesGroup.clear()

def getPriority(letter):
    if ((ord(letter)) > 96):
       return (int(ord(letter)-96))
    elif (ord(letter) < 91):
      return (int(ord(letter)-38))    

sum = 0
for badge in badges:
    sum += getPriority(badge)

print(sum)
