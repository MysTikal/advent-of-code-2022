with open('input', 'r') as file:
    data = file.read()

def uniqueList(list):
    return len(set(list)) == len(list)
    
def parseChar(str):
    charList = []
    for i, char in enumerate(str):
        charList.append(char)
        if len(charList) == 15:
            charList.pop(0)
        if len(charList) == 14:
            if uniqueList(charList):
                print(i+1)
                break

parseChar(data)
