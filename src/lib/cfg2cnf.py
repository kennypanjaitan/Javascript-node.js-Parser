import os

cek = {}
# READ AND WRITE --------------------
# BACA CFG.TXT
def readCFG(file):
    path = os.getcwd()
    with open(path + "/src/lib/" + file) as cfg:
        row = cfg.readlines()
        rowConverted = []
        for i in range(len(row)):
            rowConverted.append(row[i].replace("->", "").split())

        
        return rowConverted

        
        # TEST ROW CONVERTED ARRAY
        # for i in range(len(rowConverted)):
        #     print(rowConverted[i])
        # for i in range(len(row)):
        #     print(rowConverted[i])
        # print(rowConverted[2][1])

# TEST READCFG
def printGrammar(grammar):
    for grammarRule in grammar:
        for i in range(len(grammarRule)):
            if i == 0:
                print(grammarRule[i], "->", end=' ')
            else:
                print(grammarRule[i], end=' ')
        print("\n")

# BUAT CNF.TXT
def writeGrammar(grammar):
    path = os.getcwd()
    with open(path + "/src/lib/cnf.txt", "w") as cnf:
        for grammarRule in grammar:
            cnf.write(grammarRule[0] + " -> ")
            for i in grammar[1:]:
                cnf.write(str(i))
                cnf.write(" ")
            cnf.write("\n")

            # for i in range(len(grammarRule)):
            #     if i == 0:
            #         cnf.write(grammarRule[i] + " -> ")
            #     else:
            #         cnf.write(grammarRule[i] + " | ")

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
        newGrammar = []

        # 1 terminal/variabel
        if len(grammar) == 2 and not(grammar[1][0].islower()):
            unit.append(grammar)
            addGrammar(grammar)
        
        # more than 2 variabel
        while len(grammar) > 3:
            newGrammar.append([f"{grammar[0]}{str(idx)}", grammar[1], grammar[2]])
            grammar = [f"{grammar[0]}{str(idx)}", grammar[3:]]
            idx += 1
        

        if grammar:
            addGrammar(grammar)
            result.append(grammar)
        
        if newGrammar:
            for i in range(len(newGrammar)):
                result.append(newGrammar[i])
    
    # 1 variabel
    while unit:
        grammar = unit.pop()
        if grammar[1] in cek:
            for value in cek[grammar[1]]:
                newGrammar = [grammar[0]] + value

                # 2 variabel masukin ke unit, final state = jadi terminal
                if len(newGrammar) == 2 and not(newGrammar[1][0].islower()):
                    unit.append(newGrammar)
                # variabel diubah kalau ada terminal atau len > 2
                elif len(newGrammar) > 2 or newGrammar[1][0].islower():
                    result.append(newGrammar)
                addGrammar(newGrammar)
    return result
print(len(convertToCNF(readCFG("cfg.txt"))))

# /Users/kenny_bnp/Desktop/INFORMATICS ROOKIE/TBFO/TUBES/Javascript-node.js-Parser/src/lib/cfg.txt