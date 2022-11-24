# import path
import time
from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
print('WELCOME TO JAVASCRIPT (NODE.JS) SIMPLE PARSER')
print('==============================================')
fileName = input('Please enter your file name (ex : haha.js) : ')
time.sleep(0.2)
clear()

for i in range(3):
    print('Parsing ' + fileName + '...')
    print('loading.')
    time.sleep(0.5)
    clear()
    print('Parsing ' + fileName + '...')
    print('loading..')
    time.sleep(0.5)
    clear()
    print('Parsing ' + fileName + '...')
    print('loading...')
    time.sleep(0.5)
    clear()
    print('Parsing ' + fileName + '...')
    print('loading....')
    time.sleep(0.5)
    clear()