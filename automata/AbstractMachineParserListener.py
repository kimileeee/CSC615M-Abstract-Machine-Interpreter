# Generated from ./automata/AbstractMachineParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AbstractMachineParser import AbstractMachineParser
else:
    from AbstractMachineParser import AbstractMachineParser

# This class defines a complete listener for a parse tree produced by AbstractMachineParser.
class AbstractMachineParserListener(ParseTreeListener):

    # Enter a parse tree produced by AbstractMachineParser#FullProgram.
    def enterFullProgram(self, ctx:AbstractMachineParser.FullProgramContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#FullProgram.
    def exitFullProgram(self, ctx:AbstractMachineParser.FullProgramContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#IdentifierReal.
    def enterIdentifierReal(self, ctx:AbstractMachineParser.IdentifierRealContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#IdentifierReal.
    def exitIdentifierReal(self, ctx:AbstractMachineParser.IdentifierRealContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#SymbolAsIdentifier.
    def enterSymbolAsIdentifier(self, ctx:AbstractMachineParser.SymbolAsIdentifierContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#SymbolAsIdentifier.
    def exitSymbolAsIdentifier(self, ctx:AbstractMachineParser.SymbolAsIdentifierContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#memory_declaration.
    def enterMemory_declaration(self, ctx:AbstractMachineParser.Memory_declarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#memory_declaration.
    def exitMemory_declaration(self, ctx:AbstractMachineParser.Memory_declarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#CommandLogicDeclaration.
    def enterCommandLogicDeclaration(self, ctx:AbstractMachineParser.CommandLogicDeclarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#CommandLogicDeclaration.
    def exitCommandLogicDeclaration(self, ctx:AbstractMachineParser.CommandLogicDeclarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#MemoryOperationLogicDeclaration.
    def enterMemoryOperationLogicDeclaration(self, ctx:AbstractMachineParser.MemoryOperationLogicDeclarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#MemoryOperationLogicDeclaration.
    def exitMemoryOperationLogicDeclaration(self, ctx:AbstractMachineParser.MemoryOperationLogicDeclarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#MoveOverTapeLogicDeclaration.
    def enterMoveOverTapeLogicDeclaration(self, ctx:AbstractMachineParser.MoveOverTapeLogicDeclarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#MoveOverTapeLogicDeclaration.
    def exitMoveOverTapeLogicDeclaration(self, ctx:AbstractMachineParser.MoveOverTapeLogicDeclarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#ScanCommand.
    def enterScanCommand(self, ctx:AbstractMachineParser.ScanCommandContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#ScanCommand.
    def exitScanCommand(self, ctx:AbstractMachineParser.ScanCommandContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#PrintCommand.
    def enterPrintCommand(self, ctx:AbstractMachineParser.PrintCommandContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#PrintCommand.
    def exitPrintCommand(self, ctx:AbstractMachineParser.PrintCommandContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#ScanRightCommand.
    def enterScanRightCommand(self, ctx:AbstractMachineParser.ScanRightCommandContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#ScanRightCommand.
    def exitScanRightCommand(self, ctx:AbstractMachineParser.ScanRightCommandContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#ScanLeftCommand.
    def enterScanLeftCommand(self, ctx:AbstractMachineParser.ScanLeftCommandContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#ScanLeftCommand.
    def exitScanLeftCommand(self, ctx:AbstractMachineParser.ScanLeftCommandContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#memory_operation.
    def enterMemory_operation(self, ctx:AbstractMachineParser.Memory_operationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#memory_operation.
    def exitMemory_operation(self, ctx:AbstractMachineParser.Memory_operationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#tape_operation.
    def enterTape_operation(self, ctx:AbstractMachineParser.Tape_operationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#tape_operation.
    def exitTape_operation(self, ctx:AbstractMachineParser.Tape_operationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#transition.
    def enterTransition(self, ctx:AbstractMachineParser.TransitionContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#transition.
    def exitTransition(self, ctx:AbstractMachineParser.TransitionContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#replacement.
    def enterReplacement(self, ctx:AbstractMachineParser.ReplacementContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#replacement.
    def exitReplacement(self, ctx:AbstractMachineParser.ReplacementContext):
        pass



del AbstractMachineParser