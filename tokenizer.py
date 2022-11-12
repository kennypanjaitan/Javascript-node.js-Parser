import os

def token(text):
    # Read a file
    fileRead = open(text, encoding="utf8")
    char = fileRead.read()
    fileRead.close()

    # Tokenize
    tokens = # fungsi buat tokenize
    tokenHasil = []

    for token in tokens:
        tokenHasil.append(token)

    return tokenHasil

def writeFile(text, token):
    # Write a file
    path = os.getcwd()
    fileWrite = open(path + "/result/result.txt" + text, "w", encoding="utf8")
    for token in tokenHasil:
        fileWrite.write(token + " ")
        print(token)
    fileWrite.close()


    


    
