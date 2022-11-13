import os

# BACA CFG.TXT
def readCFG(file):
    path = os.getcwd()
    with open(path + "/src/lib/" + file) as cfg:
        row = cfg.readlines()
        rowConverted = []
        for i in range(len(row)):
            rowConverted.append(row[i].replace("->", "").split())

        return rowConverted
        # for i in range(len(row)):
        #     print(rowConverted[i])

# TEST READCFG
def printGrammar(grammar):
    for grammarRule in grammar:
        for i in range(len(grammarRule)):
            if i == 0:
                print(grammarRule[i], "->", end='')
            else:
                print(grammarRule[i], end=' ')
        print("\n")

# BUAT CNF.TXT
def writeGrammar(grammar):
    path = os.getcwd()
    with open(path + "/src/lib/cnf.txt", "w") as cnf:
        for grammarRule in grammar:
            for i in range(len(grammarRule)):
                if i == 0:
                    cnf.write(grammarRule[i] + " -> ")
                else:
                    cnf.write(grammarRule[i] + " | ")
            cnf.write("\n")

    # cnf = open(path + "/src/lib/cnf.txt", "w")
    # for rule in grammsar:
    #     cnf.write(rule[0])
    #     cnf.write(" -> ")
    #     for i in rule[1:]:
    #         cnf.write(i)
    #         cnf.write(" | ")
    #     cnf.write("\n")
    # cnf.close()

printGrammar(readCFG("cfg.txt"))

# /Users/kenny_bnp/Desktop/INFORMATICS ROOKIE/TBFO/TUBES/Javascript-node.js-Parser/src/lib/cfg.txt