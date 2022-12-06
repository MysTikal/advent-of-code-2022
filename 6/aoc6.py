with open('input', 'r') as file:
    data = file.read()

def parseChar(str):
    charList = []
    for i, char in enumerate(str):
        charList.append(char)
        if len(charList) == 15:
            charList.pop(0)
        if len(set(charList)) == 14:
            print(i+1)
            break

parseChar(data)
