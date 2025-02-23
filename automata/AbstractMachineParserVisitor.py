# Generated from AbstractMachineParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AbstractMachineParser import AbstractMachineParser
else:
    from AbstractMachineParser import AbstractMachineParser

# This class defines a complete generic visitor for a parse tree produced by AbstractMachineParser.

class AbstractMachineParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AbstractMachineParser#program.
    def visitProgram(self, ctx:AbstractMachineParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#Identifier.
    def visitIdentifier(self, ctx:AbstractMachineParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#SymbolAsIdentifier.
    def visitSymbolAsIdentifier(self, ctx:AbstractMachineParser.SymbolAsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#StackDeclaration.
    def visitStackDeclaration(self, ctx:AbstractMachineParser.StackDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#QueueDeclaration.
    def visitQueueDeclaration(self, ctx:AbstractMachineParser.QueueDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#TapeDeclaration.
    def visitTapeDeclaration(self, ctx:AbstractMachineParser.TapeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#logic_declaration.
    def visitLogic_declaration(self, ctx:AbstractMachineParser.Logic_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#commmand.
    def visitCommmand(self, ctx:AbstractMachineParser.CommmandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#memory_operation.
    def visitMemory_operation(self, ctx:AbstractMachineParser.Memory_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#direction.
    def visitDirection(self, ctx:AbstractMachineParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#move_over_tape.
    def visitMove_over_tape(self, ctx:AbstractMachineParser.Move_over_tapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#replacement.
    def visitReplacement(self, ctx:AbstractMachineParser.ReplacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#param_list.
    def visitParam_list(self, ctx:AbstractMachineParser.Param_listContext):
        return self.visitChildren(ctx)



del AbstractMachineParser