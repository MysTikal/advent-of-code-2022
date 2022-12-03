with open('input') as file:
    lines = [line.rstrip() for line in file]

grouped = list(zip(*(iter(lines),) * 3))
result = []
sum = 0

for group in grouped: 
    g0 = set(group[0]), 
    g1 = set(group[1]) 
    g2 = set(group[2])
    result += g0.intersection(g1, g2)

def getPriority(letter): 
    if ((ord(letter)) > 96):
       return (int(ord(letter)-96))
    elif (ord(letter) < 91):
      return (int(ord(letter)-38))    

for x in result:
    sum += getPriority(x)

print(sum)

