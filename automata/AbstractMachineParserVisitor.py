# Generated from ./automata/AbstractMachineParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AbstractMachineParser import AbstractMachineParser
else:
    from AbstractMachineParser import AbstractMachineParser

# This class defines a complete generic visitor for a parse tree produced by AbstractMachineParser.

class AbstractMachineParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AbstractMachineParser#FullProgram.
    def visitFullProgram(self, ctx:AbstractMachineParser.FullProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#IdentifierReal.
    def visitIdentifierReal(self, ctx:AbstractMachineParser.IdentifierRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#SymbolAsIdentifier.
    def visitSymbolAsIdentifier(self, ctx:AbstractMachineParser.SymbolAsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#memory_declaration.
    def visitMemory_declaration(self, ctx:AbstractMachineParser.Memory_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#CommandLogicDeclaration.
    def visitCommandLogicDeclaration(self, ctx:AbstractMachineParser.CommandLogicDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#MemoryOperationLogicDeclaration.
    def visitMemoryOperationLogicDeclaration(self, ctx:AbstractMachineParser.MemoryOperationLogicDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#MoveOverTapeLogicDeclaration.
    def visitMoveOverTapeLogicDeclaration(self, ctx:AbstractMachineParser.MoveOverTapeLogicDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#ScanCommand.
    def visitScanCommand(self, ctx:AbstractMachineParser.ScanCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#PrintCommand.
    def visitPrintCommand(self, ctx:AbstractMachineParser.PrintCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#ScanRightCommand.
    def visitScanRightCommand(self, ctx:AbstractMachineParser.ScanRightCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#ScanLeftCommand.
    def visitScanLeftCommand(self, ctx:AbstractMachineParser.ScanLeftCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#memory_operation.
    def visitMemory_operation(self, ctx:AbstractMachineParser.Memory_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#tape_operation.
    def visitTape_operation(self, ctx:AbstractMachineParser.Tape_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#transition.
    def visitTransition(self, ctx:AbstractMachineParser.TransitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbstractMachineParser#replacement.
    def visitReplacement(self, ctx:AbstractMachineParser.ReplacementContext):
        return self.visitChildren(ctx)



del AbstractMachineParser