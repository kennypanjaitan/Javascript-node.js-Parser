## Formal Languages and Automata Theory (IF2124) Project
# Parser-for-Javascript-node.js
> Project for Formal Languages and Automata Theory (IF2124) course from School of Electrical Engineering and Informatics, Bandung Institute of Technology.

### Table of Contents
* [General Info](#general-information)
* [Contributors](#contributors)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Structure](#structure)

### General Information
A Parser for Javascript (node.js) made in python. This parser applied Finite Automata (FA) state machine to evaluates variable and mathematical expression. 
This parser also applied Context Free Grammar (CFG) to evaluates syntax by converts CFG rules that were already made to Chomsky Normal Form (CNF) Grammar as an input to Cocke-Younger-Kasami (CYK) algorthm as our main algorithm.

### Contributors 
"semangatKeni" group from K3 class
- 13521006 Azmi Hasna Zahrani
- 13521013 Eunice Sarah Siregar
- 13521023 Kenny Benaya Nathan

### Technologies Used
- Pyhon

### Features
- Choose your desired javascript file to parse
- If there's no error, then the program will show that the files syntax are accepted
- if there's error, the program will show the illegal syntax or character in which line and collumn

### Setup
1. Clone this repository (First use only)
2. Change directory to src ```cd src```
3. run main.py file ```python3 main.py```

### Structure
```bash
.
├── src ------------------------------------------ Folder containing source files
│   ├── lib -------------------------------------- Folder containing algorithm and grammar
│   ├── main.py ---------------------------------- Main program
│ 
├── test --------------------------------------- Folder containing javascript files for testing
├── README.md
```
