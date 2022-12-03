with open('input') as file:
    lines = [line.rstrip() for line in file]


seenLetters = []
matchingLetters = []
priorities = []
lineMatches = []

for line in lines:
    first, second = line[:len(line)//2], line[len(line)//2:]
    
    for char in second:
        if (char in first) & (char not in lineMatches): # dont repeat matching chars in current line
            matchingLetters.append(char)
            lineMatches.append(char)
    lineMatches.clear()

def getPriority(letter):
    if ((ord(letter)) > 96):
       return (int(ord(letter)-96))
    elif (ord(letter) < 91):
      return (int(ord(letter)-38))    

for letter in matchingLetters:
    priorities.append(getPriority(letter))

print(lines)
print(priorities)
print(sum(priorities))

