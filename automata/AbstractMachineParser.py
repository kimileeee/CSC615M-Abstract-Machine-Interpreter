# Generated from ./automata/AbstractMachineParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,139,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,4,0,21,8,0,11,0,12,0,22,5,0,25,8,0,10,
        0,12,0,28,9,0,1,0,1,0,4,0,32,8,0,11,0,12,0,33,1,1,1,1,3,1,38,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,5,3,56,8,3,10,3,12,3,59,9,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,67,8,3,
        10,3,12,3,70,9,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,78,8,3,10,3,12,3,81,
        9,3,3,3,83,8,3,1,4,1,4,1,4,1,4,3,4,89,8,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,101,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,123,8,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,0,0,9,0,2,
        4,6,8,10,12,14,16,0,0,148,0,26,1,0,0,0,2,37,1,0,0,0,4,47,1,0,0,0,
        6,82,1,0,0,0,8,88,1,0,0,0,10,100,1,0,0,0,12,122,1,0,0,0,14,124,1,
        0,0,0,16,130,1,0,0,0,18,20,5,1,0,0,19,21,3,4,2,0,20,19,1,0,0,0,21,
        22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,18,1,0,0,
        0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,
        1,0,0,0,29,31,5,6,0,0,30,32,3,6,3,0,31,30,1,0,0,0,32,33,1,0,0,0,
        33,31,1,0,0,0,33,34,1,0,0,0,34,1,1,0,0,0,35,38,5,23,0,0,36,38,5,
        22,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,40,5,2,0,0,40,
        48,5,23,0,0,41,42,5,3,0,0,42,48,5,23,0,0,43,44,5,4,0,0,44,48,5,23,
        0,0,45,46,5,5,0,0,46,48,5,23,0,0,47,39,1,0,0,0,47,41,1,0,0,0,47,
        43,1,0,0,0,47,45,1,0,0,0,48,5,1,0,0,0,49,50,3,2,1,0,50,51,5,18,0,
        0,51,52,3,8,4,0,52,57,3,14,7,0,53,54,5,17,0,0,54,56,3,14,7,0,55,
        53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,83,1,0,0,
        0,59,57,1,0,0,0,60,61,3,2,1,0,61,62,5,18,0,0,62,63,3,10,5,0,63,68,
        3,14,7,0,64,65,5,17,0,0,65,67,3,14,7,0,66,64,1,0,0,0,67,70,1,0,0,
        0,68,66,1,0,0,0,68,69,1,0,0,0,69,83,1,0,0,0,70,68,1,0,0,0,71,72,
        3,2,1,0,72,73,5,18,0,0,73,74,3,12,6,0,74,79,3,16,8,0,75,76,5,17,
        0,0,76,78,3,16,8,0,77,75,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,
        80,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,82,49,1,0,0,0,82,60,1,0,0,
        0,82,71,1,0,0,0,83,7,1,0,0,0,84,89,5,7,0,0,85,89,5,8,0,0,86,89,5,
        9,0,0,87,89,5,10,0,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,88,
        87,1,0,0,0,89,9,1,0,0,0,90,91,5,11,0,0,91,92,5,19,0,0,92,93,3,2,
        1,0,93,94,5,20,0,0,94,101,1,0,0,0,95,96,5,12,0,0,96,97,5,19,0,0,
        97,98,3,2,1,0,98,99,5,20,0,0,99,101,1,0,0,0,100,90,1,0,0,0,100,95,
        1,0,0,0,101,11,1,0,0,0,102,103,5,13,0,0,103,104,5,19,0,0,104,105,
        3,2,1,0,105,106,5,20,0,0,106,123,1,0,0,0,107,108,5,14,0,0,108,109,
        5,19,0,0,109,110,3,2,1,0,110,111,5,20,0,0,111,123,1,0,0,0,112,113,
        5,15,0,0,113,114,5,19,0,0,114,115,3,2,1,0,115,116,5,20,0,0,116,123,
        1,0,0,0,117,118,5,16,0,0,118,119,5,19,0,0,119,120,3,2,1,0,120,121,
        5,20,0,0,121,123,1,0,0,0,122,102,1,0,0,0,122,107,1,0,0,0,122,112,
        1,0,0,0,122,117,1,0,0,0,123,13,1,0,0,0,124,125,5,19,0,0,125,126,
        5,22,0,0,126,127,5,17,0,0,127,128,3,2,1,0,128,129,5,20,0,0,129,15,
        1,0,0,0,130,131,5,19,0,0,131,132,5,22,0,0,132,133,5,21,0,0,133,134,
        5,22,0,0,134,135,5,17,0,0,135,136,3,2,1,0,136,137,5,20,0,0,137,17,
        1,0,0,0,12,22,26,33,37,47,57,68,79,82,88,100,122
    ]

class AbstractMachineParser ( Parser ):

    grammarFileName = "AbstractMachineParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.DATA'", "'STACK'", "'QUEUE'", "'TAPE'", 
                     "'2D_TAPE'", "'.LOGIC'", "'SCAN'", "'PRINT'", "'SCAN RIGHT'", 
                     "'SCAN LEFT'", "'READ'", "'WRITE'", "'RIGHT'", "'LEFT'", 
                     "'UP'", "'DOWN'", "','", "']'", "'('", "')'", "'/'" ]

    symbolicNames = [ "<INVALID>", "DATA", "STACK", "QUEUE", "TAPE", "TAPE_2D", 
                      "LOGIC", "SCAN", "PRINT", "SCAN_RIGHT", "SCAN_LEFT", 
                      "READ", "WRITE", "RIGHT", "LEFT", "UP", "DOWN", "COMMA", 
                      "CLOSE_BRACKET", "OPEN_PAR", "CLOSE_PAR", "SLASH", 
                      "SYMBOL", "IDENTIFIER", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_identifier = 1
    RULE_memory_declaration = 2
    RULE_logic_declaration = 3
    RULE_command = 4
    RULE_memory_operation = 5
    RULE_tape_operation = 6
    RULE_transition = 7
    RULE_replacement = 8

    ruleNames =  [ "program", "identifier", "memory_declaration", "logic_declaration", 
                   "command", "memory_operation", "tape_operation", "transition", 
                   "replacement" ]

    EOF = Token.EOF
    DATA=1
    STACK=2
    QUEUE=3
    TAPE=4
    TAPE_2D=5
    LOGIC=6
    SCAN=7
    PRINT=8
    SCAN_RIGHT=9
    SCAN_LEFT=10
    READ=11
    WRITE=12
    RIGHT=13
    LEFT=14
    UP=15
    DOWN=16
    COMMA=17
    CLOSE_BRACKET=18
    OPEN_PAR=19
    CLOSE_PAR=20
    SLASH=21
    SYMBOL=22
    IDENTIFIER=23
    COMMENT=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FullProgramContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGIC(self):
            return self.getToken(AbstractMachineParser.LOGIC, 0)
        def DATA(self, i:int=None):
            if i is None:
                return self.getTokens(AbstractMachineParser.DATA)
            else:
                return self.getToken(AbstractMachineParser.DATA, i)
        def logic_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.Logic_declarationContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.Logic_declarationContext,i)

        def memory_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.Memory_declarationContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.Memory_declarationContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullProgram" ):
                listener.enterFullProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullProgram" ):
                listener.exitFullProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullProgram" ):
                return visitor.visitFullProgram(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = AbstractMachineParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = AbstractMachineParser.FullProgramContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 18
                self.match(AbstractMachineParser.DATA)
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 19
                    self.memory_declaration()
                    self.state = 22 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                        break

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(AbstractMachineParser.LOGIC)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.logic_declaration()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22 or _la==23):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_identifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SymbolAsIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.IdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SYMBOL(self):
            return self.getToken(AbstractMachineParser.SYMBOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbolAsIdentifier" ):
                listener.enterSymbolAsIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbolAsIdentifier" ):
                listener.exitSymbolAsIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbolAsIdentifier" ):
                return visitor.visitSymbolAsIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierRealContext(IdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.IdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierReal" ):
                listener.enterIdentifierReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierReal" ):
                listener.exitIdentifierReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierReal" ):
                return visitor.visitIdentifierReal(self)
            else:
                return visitor.visitChildren(self)



    def identifier(self):

        localctx = AbstractMachineParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_identifier)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = AbstractMachineParser.IdentifierRealContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            elif token in [22]:
                localctx = AbstractMachineParser.SymbolAsIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(AbstractMachineParser.SYMBOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Memory_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STACK(self):
            return self.getToken(AbstractMachineParser.STACK, 0)

        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

        def QUEUE(self):
            return self.getToken(AbstractMachineParser.QUEUE, 0)

        def TAPE(self):
            return self.getToken(AbstractMachineParser.TAPE, 0)

        def TAPE_2D(self):
            return self.getToken(AbstractMachineParser.TAPE_2D, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_memory_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemory_declaration" ):
                listener.enterMemory_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemory_declaration" ):
                listener.exitMemory_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemory_declaration" ):
                return visitor.visitMemory_declaration(self)
            else:
                return visitor.visitChildren(self)




    def memory_declaration(self):

        localctx = AbstractMachineParser.Memory_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memory_declaration)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(AbstractMachineParser.STACK)
                self.state = 40
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(AbstractMachineParser.QUEUE)
                self.state = 42
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(AbstractMachineParser.TAPE)
                self.state = 44
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(AbstractMachineParser.TAPE_2D)
                self.state = 46
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_logic_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CommandLogicDeclarationContext(Logic_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.Logic_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentifierContext,0)

        def CLOSE_BRACKET(self):
            return self.getToken(AbstractMachineParser.CLOSE_BRACKET, 0)
        def command(self):
            return self.getTypedRuleContext(AbstractMachineParser.CommandContext,0)

        def transition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.TransitionContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.TransitionContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AbstractMachineParser.COMMA)
            else:
                return self.getToken(AbstractMachineParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandLogicDeclaration" ):
                listener.enterCommandLogicDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandLogicDeclaration" ):
                listener.exitCommandLogicDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandLogicDeclaration" ):
                return visitor.visitCommandLogicDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class MoveOverTapeLogicDeclarationContext(Logic_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.Logic_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentifierContext,0)

        def CLOSE_BRACKET(self):
            return self.getToken(AbstractMachineParser.CLOSE_BRACKET, 0)
        def tape_operation(self):
            return self.getTypedRuleContext(AbstractMachineParser.Tape_operationContext,0)

        def replacement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.ReplacementContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.ReplacementContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AbstractMachineParser.COMMA)
            else:
                return self.getToken(AbstractMachineParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveOverTapeLogicDeclaration" ):
                listener.enterMoveOverTapeLogicDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveOverTapeLogicDeclaration" ):
                listener.exitMoveOverTapeLogicDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveOverTapeLogicDeclaration" ):
                return visitor.visitMoveOverTapeLogicDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class MemoryOperationLogicDeclarationContext(Logic_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.Logic_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentifierContext,0)

        def CLOSE_BRACKET(self):
            return self.getToken(AbstractMachineParser.CLOSE_BRACKET, 0)
        def memory_operation(self):
            return self.getTypedRuleContext(AbstractMachineParser.Memory_operationContext,0)

        def transition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.TransitionContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.TransitionContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AbstractMachineParser.COMMA)
            else:
                return self.getToken(AbstractMachineParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemoryOperationLogicDeclaration" ):
                listener.enterMemoryOperationLogicDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemoryOperationLogicDeclaration" ):
                listener.exitMemoryOperationLogicDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemoryOperationLogicDeclaration" ):
                return visitor.visitMemoryOperationLogicDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def logic_declaration(self):

        localctx = AbstractMachineParser.Logic_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_logic_declaration)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = AbstractMachineParser.CommandLogicDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.identifier()
                self.state = 50
                self.match(AbstractMachineParser.CLOSE_BRACKET)
                self.state = 51
                self.command()
                self.state = 52
                self.transition()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 53
                    self.match(AbstractMachineParser.COMMA)
                    self.state = 54
                    self.transition()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = AbstractMachineParser.MemoryOperationLogicDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.identifier()
                self.state = 61
                self.match(AbstractMachineParser.CLOSE_BRACKET)
                self.state = 62
                self.memory_operation()
                self.state = 63
                self.transition()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 64
                    self.match(AbstractMachineParser.COMMA)
                    self.state = 65
                    self.transition()
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                localctx = AbstractMachineParser.MoveOverTapeLogicDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.identifier()
                self.state = 72
                self.match(AbstractMachineParser.CLOSE_BRACKET)
                self.state = 73
                self.tape_operation()
                self.state = 74
                self.replacement()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 75
                    self.match(AbstractMachineParser.COMMA)
                    self.state = 76
                    self.replacement()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ScanRightCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCAN_RIGHT(self):
            return self.getToken(AbstractMachineParser.SCAN_RIGHT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanRightCommand" ):
                listener.enterScanRightCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanRightCommand" ):
                listener.exitScanRightCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanRightCommand" ):
                return visitor.visitScanRightCommand(self)
            else:
                return visitor.visitChildren(self)


    class ScanCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCAN(self):
            return self.getToken(AbstractMachineParser.SCAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanCommand" ):
                listener.enterScanCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanCommand" ):
                listener.exitScanCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanCommand" ):
                return visitor.visitScanCommand(self)
            else:
                return visitor.visitChildren(self)


    class PrintCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(AbstractMachineParser.PRINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintCommand" ):
                listener.enterPrintCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintCommand" ):
                listener.exitPrintCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintCommand" ):
                return visitor.visitPrintCommand(self)
            else:
                return visitor.visitChildren(self)


    class ScanLeftCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCAN_LEFT(self):
            return self.getToken(AbstractMachineParser.SCAN_LEFT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanLeftCommand" ):
                listener.enterScanLeftCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanLeftCommand" ):
                listener.exitScanLeftCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanLeftCommand" ):
                return visitor.visitScanLeftCommand(self)
            else:
                return visitor.visitChildren(self)



    def command(self):

        localctx = AbstractMachineParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_command)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = AbstractMachineParser.ScanCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(AbstractMachineParser.SCAN)
                pass
            elif token in [8]:
                localctx = AbstractMachineParser.PrintCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(AbstractMachineParser.PRINT)
                pass
            elif token in [9]:
                localctx = AbstractMachineParser.ScanRightCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(AbstractMachineParser.SCAN_RIGHT)
                pass
            elif token in [10]:
                localctx = AbstractMachineParser.ScanLeftCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.match(AbstractMachineParser.SCAN_LEFT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Memory_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(AbstractMachineParser.READ, 0)

        def OPEN_PAR(self):
            return self.getToken(AbstractMachineParser.OPEN_PAR, 0)

        def identifier(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentifierContext,0)


        def CLOSE_PAR(self):
            return self.getToken(AbstractMachineParser.CLOSE_PAR, 0)

        def WRITE(self):
            return self.getToken(AbstractMachineParser.WRITE, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_memory_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemory_operation" ):
                listener.enterMemory_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemory_operation" ):
                listener.exitMemory_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemory_operation" ):
                return visitor.visitMemory_operation(self)
            else:
                return visitor.visitChildren(self)




    def memory_operation(self):

        localctx = AbstractMachineParser.Memory_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_memory_operation)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(AbstractMachineParser.READ)
                self.state = 91
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 92
                self.identifier()
                self.state = 93
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(AbstractMachineParser.WRITE)
                self.state = 96
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 97
                self.identifier()
                self.state = 98
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tape_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RIGHT(self):
            return self.getToken(AbstractMachineParser.RIGHT, 0)

        def OPEN_PAR(self):
            return self.getToken(AbstractMachineParser.OPEN_PAR, 0)

        def identifier(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentifierContext,0)


        def CLOSE_PAR(self):
            return self.getToken(AbstractMachineParser.CLOSE_PAR, 0)

        def LEFT(self):
            return self.getToken(AbstractMachineParser.LEFT, 0)

        def UP(self):
            return self.getToken(AbstractMachineParser.UP, 0)

        def DOWN(self):
            return self.getToken(AbstractMachineParser.DOWN, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_tape_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTape_operation" ):
                listener.enterTape_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTape_operation" ):
                listener.exitTape_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTape_operation" ):
                return visitor.visitTape_operation(self)
            else:
                return visitor.visitChildren(self)




    def tape_operation(self):

        localctx = AbstractMachineParser.Tape_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tape_operation)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(AbstractMachineParser.RIGHT)
                self.state = 103
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 104
                self.identifier()
                self.state = 105
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(AbstractMachineParser.LEFT)
                self.state = 108
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 109
                self.identifier()
                self.state = 110
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.match(AbstractMachineParser.UP)
                self.state = 113
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 114
                self.identifier()
                self.state = 115
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.match(AbstractMachineParser.DOWN)
                self.state = 118
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 119
                self.identifier()
                self.state = 120
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAR(self):
            return self.getToken(AbstractMachineParser.OPEN_PAR, 0)

        def SYMBOL(self):
            return self.getToken(AbstractMachineParser.SYMBOL, 0)

        def COMMA(self):
            return self.getToken(AbstractMachineParser.COMMA, 0)

        def identifier(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentifierContext,0)


        def CLOSE_PAR(self):
            return self.getToken(AbstractMachineParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_transition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransition" ):
                listener.enterTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransition" ):
                listener.exitTransition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransition" ):
                return visitor.visitTransition(self)
            else:
                return visitor.visitChildren(self)




    def transition(self):

        localctx = AbstractMachineParser.TransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_transition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(AbstractMachineParser.OPEN_PAR)
            self.state = 125
            self.match(AbstractMachineParser.SYMBOL)
            self.state = 126
            self.match(AbstractMachineParser.COMMA)
            self.state = 127
            self.identifier()
            self.state = 128
            self.match(AbstractMachineParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReplacementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAR(self):
            return self.getToken(AbstractMachineParser.OPEN_PAR, 0)

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(AbstractMachineParser.SYMBOL)
            else:
                return self.getToken(AbstractMachineParser.SYMBOL, i)

        def SLASH(self):
            return self.getToken(AbstractMachineParser.SLASH, 0)

        def COMMA(self):
            return self.getToken(AbstractMachineParser.COMMA, 0)

        def identifier(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentifierContext,0)


        def CLOSE_PAR(self):
            return self.getToken(AbstractMachineParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_replacement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplacement" ):
                listener.enterReplacement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplacement" ):
                listener.exitReplacement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplacement" ):
                return visitor.visitReplacement(self)
            else:
                return visitor.visitChildren(self)




    def replacement(self):

        localctx = AbstractMachineParser.ReplacementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_replacement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(AbstractMachineParser.OPEN_PAR)
            self.state = 131
            self.match(AbstractMachineParser.SYMBOL)
            self.state = 132
            self.match(AbstractMachineParser.SLASH)
            self.state = 133
            self.match(AbstractMachineParser.SYMBOL)
            self.state = 134
            self.match(AbstractMachineParser.COMMA)
            self.state = 135
            self.identifier()
            self.state = 136
            self.match(AbstractMachineParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





