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

### 2. Visualizing the Parse Tree

To visualize the parse tree for a sample code file, use:

```bash
antlr4-parse ./automata/AbstractMachineParser.g4 ./automata/AbstractMachineLexer.g4 program -gui ./samples/sample06.txt
```

This command opens a GUI displaying the parse tree for the `sample06.txt` file. You can modify the command to parse other sample files in the `samples/` folder.

### 3. Running the Main Program in `main.py`

To run the main program and execute the interpreter for a given board game source code, use:

```bash
python main.py -F ./samples/sample06.txt
```

This will run the `interpreter.py` script with the specified source code file (in this case, `sample06.txt`) from the `samples/` directory. You can replace the path with any other sample file or custom board game source code file. The program will parse the input and interpret the board game logic according to the grammar definitions.
