import sys
import re
import os
from sym import syms

def lexer(string, syms):
    position = 0
    tokens = [[]]
    line = 1
    found = None
    while position < len(string):
        if string[position] == "\n":
            line = line + 1
            tokens.append([])
        for sym in syms:
            patt, tag = sym
            regex = re.compile(patt)
            found = regex.match(string, position)
            if found:
                word = found.group(0)
                if tag:
                    token = word, tag
                    tokens[line].append(token)
                break
        if not found:
            print("Syntax Error")
            print(f"Illegal character found at line {line}")
            sys.exit(1)
        else:
            position = found.end(0)
    return tokens   

def CreateToken(string):
    path = os.getcwd()
    openfile = open(path + string, encoding="utf8")
    char = openfile.read()
    openfile.close()
    tokens = lexer(char, syms)
    result = []

    for token in tokens:
        result.append(token)
    
    path = os.getcwd
    write = open(path + "\\result.txt")
    for token in result:
        write.write(str(token) + " ")
    write.close()

    return result