# CSC615M-Abstract-Machine-Interpreter
 
## Installation

Before running the code, ensure the following Python packages are installed:

```bash
pip install antlr4-python3-runtime antlr4-tools tabulate ttkthemes
```

## Getting Started

### 1. Compiling Lexer and Parser Files

To compile the lexer and parser files from the grammar definitions, use ANTLR:

```bash
antlr4 -Dlanguage=Python3 ./automata/AbstractMachineLexer.g4 -o ./automata
antlr4 -Dlanguage=Python3 ./automata/AbstractMachineParser.g4 -o ./automata -visitor
```

### 2. Running the Main Program in `main.py`

To run the main program and execute the interpreter, use:

```bash
python main.py
```
