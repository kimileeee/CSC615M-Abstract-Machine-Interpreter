from antlr4 import *
from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor
from AbstractMachineInterpreter import AbstractMachineInterpreter
from datetime import *
import argparse
from tabulate import tabulate


def check_lexer(tokens):
    lexer_bool = True
    for token in tokens:
        if (token.channel == AbstractMachineLexer.ERRORS):
            print(f"Line {token.line}, Column {token.column}: Invalid token \'{token.text}\'")
            lexer_bool = False

    return lexer_bool

def print_token_table(lexer, token_stream):
    tokens = token_stream.tokens

    board_game_tokens = []
    tokenizer_headers = ["Line Number", "Column Start", "Column End", "Token", "Type"]

    # Loop through all tokens
    for token in tokens:
        if (token.channel == AbstractMachineLexer.ERRORS):
            print(f"Line {token.line}:{token.column} Invalid token \'{token.text}\'")
        else:
            board_game_tokens.append([token.line, token.column, token.column+len(token.text), token.text, lexer.symbolicNames[token.type]])
    
    print(tabulate(board_game_tokens, headers=tokenizer_headers, numalign="left"))

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-f', type=str, help='Your board game source code file', 
                           default='./samples/sample01.txt')
    args = argparser.parse_args()

    with open(args.f, 'r') as file:
        source_code = file.read()
        print()

        input_stream = InputStream(source_code)

        lexer = AbstractMachineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        # print_token_table(lexer, token_stream)

        # Check for lexer errors
        if check_lexer(token_stream.tokens):
            parser = AbstractMachineParser(token_stream)

            try:
                tree = parser.program()
            except Exception as e:
                print(e)

            # Interpret source code
            interpretor = AbstractMachineInterpreter()
            interpretor.visit(tree)

            interpretor.run_gui()

            # input_string = input("\nInput: ")
            # print(interpretor.run_machine(input_string))

        else:
            print("\nLexical errors found. Please check your source code.")

if __name__ == '__main__':
    main()