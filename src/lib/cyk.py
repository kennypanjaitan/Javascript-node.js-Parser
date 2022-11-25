def cyk_parse(string, cnf):
    global table
    table = [[set([]) for j in range(len(string))] for i in range(len(string))]

    for j in range(len(string)):
        print(cnf)
        for lhs, rules in cnf.items():
            for rhs in rules:
                if len(rhs) == 1  & rhs[0] == string[j]:
                    table[j][j].add(lhs)

    for i in range(j, -1, -1):
        for k in range(i, j):
            for lhs, rules in cnf.items():
                for rhs in rules:
                    if (len(rhs) == 2):
                        if (rhs[0] in table[i][k]):
                            if (rhs[1] in table[k + 1][j]):
                                table[i][j].add(lhs)
    
    # return len(table[0][len(string) - 1]) != 0 

# def message():
    if "S" in table[0][len(string) - 1]:
        print("Compile Succeed!")
    else:
        print("Compile failed ):")