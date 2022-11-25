import os

def readCFG(file):
    path = os.getcwd()
    with open(path + "/src/lib/" + file) as cfg:
        row = cfg.readlines()
        rowConverted = []
        for i in range(len(row)):
            rowConverted.append(row[i].replace("->", "").split())

        
        return rowConverted

def terminal(grammar):
    terminal_list = [
        "COLON",
        "SEMICOLON",
        "LB",
        "RB",
        "LESS",
        "MORE",
        "LESSEQ",
        "MOREEQ",
        "EQ",
        "NOTEQ",
        "SUBEQ",
        "DIVEQ",
        "MULTEQ",
        "MODEQ",
        "POWEQ",
        "SUMEQ",
        "SUB",
        "POW",
        "LCB",
        "RCB",
        "MUL",
        "DOT",
        "COMMA",
        "MOD",
        "LOGOR",
        "LOGNOT",
        "EQTO",
        "LOGAND",
        "NOT",
        "LLB",
        "RLB",
        "INCR",
        "DECR",
        "DOUBLESTR",
        "SINGLESTR",
        "SINGLECOMM",
        "MULTICOMM",
        "TERN",
        "AND",
        "OR",
        "NOT",
        "XOR",
        "LS",
        "RS",
        "URS",
        "EQVALTYPE",
        "NOTEQVALTYPE",
        "OR",
        "AND",
        "IF",
        "NOT",
        "THEN",
        "ELSE",
        "WHILE",
        "DO",
        "FALSE",
        "CONTINUE",
        "BREAK",
        "FOR",
        "TRY",
        "CATCH",
        "THROW",
        "VAR",
        "CONST",
        "LET",
        "FINALLY",
        "DEFAULT",
        "FUNCTION",
        "CASE",
        "SWITCH",
        "RETURN",
        "ELSE",
        "NULL",
        "BOOL",
        "CLASS",
        "INT",
        "STR",
        "LIST", 
        "FLOAT",
        "TYPE",
        "NUM",
        "ID",
    ]
    return grammar in terminal_list

def variable(grammar):
    return not terminal(grammar)