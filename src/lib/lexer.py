import sys
import re
import os
from lib.sym import syms

def lexer(string, syms):
    position = 0
    collumn = 1
    tokens = []
    row = 1
    while position < len(string):
        if string[position] == "\n":
            row = row + 1
            collumn = 1
            print(position)
        for sym in syms:
            patt, tag = sym
            regex = re.compile(patt)
            found = regex.match(string, position)
            if found:
                # word = found.group(0)
                if tag:
                    token = tag
                    tokens.append(token)
                break
        if not found:
            print(string[position])
            print("Syntax Error")
            print(f"Illegal character found at line {row} and coll {collumn}")
            sys.exit(1)
        else:
            position = found.end(0)
            collumn += 1
    return tokens   

def createToken(string):
    path = os.getcwd()
    openfile = open(path + '/test/' + string, encoding="utf8")
    char = openfile.read()
    openfile.close()
    tokens = lexer(char, syms)
    result = []

    for token in tokens:
        result.append(token)
    
    # path = os.getcwd
    # write = open(path + "\\result.txt")
    # for token in result:
    #     write.write(str(token) + " ")
    # write.close()

    return result