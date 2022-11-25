import os

cek = {}
# READ AND WRITE --------------------
# BACA CFG.TXT
def readCFG(file):
    path = os.getcwd()
    with open(path + '/src/lib/' + file) as cfg:
        row = cfg.readlines()
        rowConverted = []
        for i in range(len(row)):
            rowConverted.append(row[i].replace("->", "").split())
        return rowConverted

# TEST READCFG
def printGrammar(grammars):
    for grammar in grammars:
        for i in range(len(grammar)):
            if i == 0:
                print(grammar[i], "->", end=' ')
            else:
                print(grammar[i], end=' ')
        print("\n")

# BUAT CNF.TXT
def writeGrammar(grammars):
    path = os.getcwd()
    cnf = open(path + '/src/lib/' + 'cnf.txt', 'w')
    for rule in grammars:
        cnf.write(rule[0])
        cnf.write(" -> ")
        for i in rule[1:]:
            cnf.write(str(i))
            cnf.write(" ")
        cnf.write("\n")
    cnf.close()

# MAIN --------------------
def addGrammar(grammar):
    global cek
    if grammar[0] not in cek:
        cek[grammar[0]] = []
    cek[grammar[0]].append(grammar[1:])

def convertToCNF(grammars):
    global cek
    unit = []
    result = []
    idx = 0
    for grammar in grammars:
        newGrammars = []

        # 1 variabel
        if len(grammar) == 2 and grammar[1][0] != "'":
            unit.append(grammar)
            addGrammar(grammar)
            continue
        # more than 2 variabel
        while len(grammar) > 3:
            newGrammars.append([f"{grammar[0]}{str(idx)}", grammar[1], grammar[2]])
            grammar = [grammar[0]] + [f"{grammar[0]}{str(idx)}"] + grammar[3:]
            idx += 1
        
        if grammar:
            addGrammar(grammar)
            result.append(grammar)
        
        if newGrammars:
            for i in range(len(newGrammars)):
                result.append(newGrammars[i])
    
    # 1 variabel
    while unit:
        # for i in range(len(unit)):
        #     print(unit[i])
        grammar = unit.pop()
        if grammar[1] in cek:
            for value in cek[grammar[1]]:
                newGrammar = [grammar[0]] + value
                
                # variabel diubah kalau ada terminal atau len > 2
                if len(newGrammar) > 2 or newGrammar[1][0] == "'":
                    result.append(newGrammar)
                            
                # 2 variabel masukin ke unit, final state = jadi terminal
                else:
                    unit.append(newGrammar)
                addGrammar(newGrammar)
        # print("====================")
    # print("unit----------------")
    # for i in range(len(unit)):
    #     print(unit[i])
    
    # print("newGrammar------------------")
    # for i in range(len(newGrammars)):
    #     print(newGrammars[i])
    
    # print("grammars------------------")
    # for i in range(len(grammars)):
    #     print(grammars[i])
    
    # print("result------------------")
    # for i in range(len(result)):
    #     print(result[i])
    
    return result

# writeGrammar(convertToCNF(readCFG("cfg.txt")))

def mapGrammar(grammars):
    # length = len(grammars)
    map = {}
    for rule in grammars:
        map[str(rule[0])] = []
    for rule in grammars:
        elemen = []
        for idxrule in range(1, len(rule)):
            apd = rule[idxrule]
            elemen.append(apd)
        map[str(rule[0])].append(elemen)