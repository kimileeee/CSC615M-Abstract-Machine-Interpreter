# Generated from AbstractMachineParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AbstractMachineParser import AbstractMachineParser
else:
    from AbstractMachineParser import AbstractMachineParser

# This class defines a complete listener for a parse tree produced by AbstractMachineParser.
class AbstractMachineParserListener(ParseTreeListener):

    # Enter a parse tree produced by AbstractMachineParser#program.
    def enterProgram(self, ctx:AbstractMachineParser.ProgramContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#program.
    def exitProgram(self, ctx:AbstractMachineParser.ProgramContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#Identifier.
    def enterIdentifier(self, ctx:AbstractMachineParser.IdentifierContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#Identifier.
    def exitIdentifier(self, ctx:AbstractMachineParser.IdentifierContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#SymbolAsIdentifier.
    def enterSymbolAsIdentifier(self, ctx:AbstractMachineParser.SymbolAsIdentifierContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#SymbolAsIdentifier.
    def exitSymbolAsIdentifier(self, ctx:AbstractMachineParser.SymbolAsIdentifierContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#StackDeclaration.
    def enterStackDeclaration(self, ctx:AbstractMachineParser.StackDeclarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#StackDeclaration.
    def exitStackDeclaration(self, ctx:AbstractMachineParser.StackDeclarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#QueueDeclaration.
    def enterQueueDeclaration(self, ctx:AbstractMachineParser.QueueDeclarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#QueueDeclaration.
    def exitQueueDeclaration(self, ctx:AbstractMachineParser.QueueDeclarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#TapeDeclaration.
    def enterTapeDeclaration(self, ctx:AbstractMachineParser.TapeDeclarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#TapeDeclaration.
    def exitTapeDeclaration(self, ctx:AbstractMachineParser.TapeDeclarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#logic_declaration.
    def enterLogic_declaration(self, ctx:AbstractMachineParser.Logic_declarationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#logic_declaration.
    def exitLogic_declaration(self, ctx:AbstractMachineParser.Logic_declarationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#commmand.
    def enterCommmand(self, ctx:AbstractMachineParser.CommmandContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#commmand.
    def exitCommmand(self, ctx:AbstractMachineParser.CommmandContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#memory_operation.
    def enterMemory_operation(self, ctx:AbstractMachineParser.Memory_operationContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#memory_operation.
    def exitMemory_operation(self, ctx:AbstractMachineParser.Memory_operationContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#direction.
    def enterDirection(self, ctx:AbstractMachineParser.DirectionContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#direction.
    def exitDirection(self, ctx:AbstractMachineParser.DirectionContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#move_over_tape.
    def enterMove_over_tape(self, ctx:AbstractMachineParser.Move_over_tapeContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#move_over_tape.
    def exitMove_over_tape(self, ctx:AbstractMachineParser.Move_over_tapeContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#replacement.
    def enterReplacement(self, ctx:AbstractMachineParser.ReplacementContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#replacement.
    def exitReplacement(self, ctx:AbstractMachineParser.ReplacementContext):
        pass


    # Enter a parse tree produced by AbstractMachineParser#param_list.
    def enterParam_list(self, ctx:AbstractMachineParser.Param_listContext):
        pass

    # Exit a parse tree produced by AbstractMachineParser#param_list.
    def exitParam_list(self, ctx:AbstractMachineParser.Param_listContext):
        pass



del AbstractMachineParser