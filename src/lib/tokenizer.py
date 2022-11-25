import os 

def token(text):
    global tokenHasil
    # Read a file
    path = os.getcwd()
    fileRead = open(path + "/test/" + text, encoding="utf8")
    char = fileRead.read()
    fileRead.close()

    print(path)
    # Tokenize
    # tokens = # fungsi buat tokenize
    tokenHasil = []

    for token in char:
        tokenHasil.append(token)

    # return tokenHasil
    for i in range(len(tokenHasil)):
        print(tokenHasil[i])

def writeFile(text, token):
    global tokenHasil
    # Write a file
    path = os.getcwd()
    fileWrite = open(path + "/result/result.txt" + text, "w", encoding="utf8")
    for token in tokenHasil:
        fileWrite.write(token + "\n")
        print(token)
    fileWrite.close()

token('inputAcc.js')