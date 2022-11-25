# import path
import time
from os import name, system
from lib.cyk import cyk_parse
from lib.lexer import *
from lib.cfg2cnf import *

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def banner():
    print('==============================================')
    print('WELCOME TO JAVASCRIPT (NODE.JS) SIMPLE PARSER')
    print('==============================================')

clear()
banner()
fileName = input('Please enter your file name (ex : haha.js) : ')
time.sleep(0.2)
clear()

banner()
print('Reading file...')

CNF = mapGrammar(convertToCNF(readCFG('cfg.txt')))
token = createToken(fileName)
token = [x.lower() for x in token]

# print(CNF)
cyk_parse(token, CNF)