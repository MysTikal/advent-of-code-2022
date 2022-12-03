with open('input') as file:
    lines = [line.rstrip() for line in file]

answers = {
    "A X" : [1+3, 3+0], "B X" : [1+0, 1+0],  "C X" : [1+6, 2+0],
    "A Y" : [2+6, 1+3], "B Y" : [2+3, 2+3],  "C Y" : [2+0, 3+3],
    "A Z" : [3+0, 2+6], "B Z" : [3+6, 3+6],  "C Z" : [3+3, 1+6],
}

print(*(sum(answers[l][p] for l in lines) for p in (0, 1)))