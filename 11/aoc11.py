import re
import math
input = [l.strip("\n") for l in open("input").readlines()]

def initMonkeys():
    monkeys = [], [], [], [], [], [], [], []
    for idx, i in enumerate(input): 
        if idx % 7 == 0:
            id = int(str(input[idx])[-2])
            monkeys[id].append(str(id))
        if idx % 7 - 1 == 0:
            monkeys[id].append([s for s in re.findall(r'-?\d+\.?\d*', input[idx])])
        if idx % 7 - 2 == 0:
            monkeys[id].append(str(input[idx])[23:])
        if idx % 7 - 3 == 0:
            monkeys[id].append(str(input[idx])[21:])
        if idx % 7 - 4 == 0:
            monkeys[id].append(str(input[idx])[29:])
        if idx % 7 - 5 == 0:
            #print("Appending "+ str(input[idx])[30:])
            monkeys[id].append(str(input[idx])[30:])    
            monkeys[id].append("0") # number of inspections
    return monkeys

# 0 = id
# 1 = list of items
# 2 = operation
# 3 = test if divisible by x
# 4 = destination monkey if true
# 5 = destination monkey if false

def getLCM(monkeys):
    lcmNum = 1
    for monkey in monkeys:
        lcmNum = math.lcm(lcmNum, int(monkey[3]))
    print(lcmNum)
    return lcmNum


def doThing(modulo, monkeys):
    rounds = 10000
    count = 0
    lcm = getLCM(monkeys)
    while count < rounds:
        for id, monkey in enumerate(monkeys):
            itemid = 0
            while itemid < (len(monkeys[id][1])):
                #print("Monkey "+ str(id) + " inspects an item with a worry level of " + str(monkeys[id][1][itemid]))
                monkeys[id][6] = int(monkeys[id][6]) + 1
                if monkey[2] == "* old":
                    #print("Attempting to multiply " + str(monkeys[id][1][itemid]) + " by itself.")
                    monkeys[id][1][itemid] = int(monkeys[id][1][itemid]) * int(monkeys[id][1][itemid])
                else:                              
                    #print("evalStr = " + str(monkeys[id][1][itemid]) + " " + str(monkeys[id][2]))
                    evalStr = str(monkeys[id][1][itemid]) + str(monkeys[id][2])
                    monkeys[id][1][itemid] = eval(evalStr)
                monkeys[id][1][itemid] %= lcm  
                #print("Monkey gets bored with item. Worry level divided by 3 to " + str(monkeys[id][1][itemid]))
                if (monkeys[id][1][itemid] % int(monkeys[id][3]) == 0):
                        #print("Current worry level (" + str(monkeys[id][1][itemid]) + ") is evenly divisible by " + str(monkeys[id][3]) + ".")
                        #print("Item with worry level " + str(monkeys[id][1][itemid]) + " thrown to monkey " + monkeys[id][4] + ".")
                        monkeys[int(monkeys[id][4])][1].append(monkeys[id][1][itemid])
                        del(monkeys[id][1][itemid])
                elif (monkeys[id][1][itemid] % int(monkeys[id][3]) != 0):
                        #print("Current worry level (" + str(monkeys[id][1][itemid]) + ") is not evenly divisible by " + str(monkeys[id][3]) + ".")                
                        #print("Item with worry level " + str(monkeys[id][1][itemid]) + " thrown to monkey " + monkeys[id][5] + ".")
                        monkeys[int(monkeys[id][5])][1].append(monkeys[id][1][itemid])
                        del(monkeys[id][1][itemid])
                
            itemid += 1
        count += 1
    return monkeys
    
for x in range(1, 2):
    monkeys = doThing(x, initMonkeys())
    totals = []
    for monkey in monkeys:
        totals.append(monkey[6])
    print(totals)  

print((sorted(totals)[-2] * sorted(totals)[-1]))
