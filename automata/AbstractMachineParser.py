# Generated from AbstractMachineParser.g4 by ANTLR 4.13.2
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
        4,1,23,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,4,0,23,8,0,11,0,12,0,24,1,0,1,
        0,4,0,29,8,0,11,0,12,0,30,1,0,1,0,4,0,35,8,0,11,0,12,0,36,3,0,39,
        8,0,1,1,1,1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,51,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,5,3,59,8,3,10,3,12,3,62,9,3,1,3,1,3,1,3,1,3,1,
        3,1,3,5,3,70,8,3,10,3,12,3,73,9,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,81,
        8,3,10,3,12,3,84,9,3,3,3,86,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,98,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,123,8,9,1,9,0,
        0,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,6,9,1,0,12,15,128,0,38,1,0,
        0,0,2,42,1,0,0,0,4,50,1,0,0,0,6,85,1,0,0,0,8,87,1,0,0,0,10,97,1,
        0,0,0,12,99,1,0,0,0,14,101,1,0,0,0,16,106,1,0,0,0,18,122,1,0,0,0,
        20,22,5,1,0,0,21,23,3,4,2,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,
        0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,26,28,5,5,0,0,27,29,3,6,3,0,28,
        27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,39,1,0,0,
        0,32,34,5,5,0,0,33,35,3,6,3,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,
        1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,20,1,0,0,0,38,32,1,0,0,0,
        39,1,1,0,0,0,40,43,5,22,0,0,41,43,5,21,0,0,42,40,1,0,0,0,42,41,1,
        0,0,0,43,3,1,0,0,0,44,45,5,2,0,0,45,51,5,22,0,0,46,47,5,3,0,0,47,
        51,5,22,0,0,48,49,5,4,0,0,49,51,5,22,0,0,50,44,1,0,0,0,50,46,1,0,
        0,0,50,48,1,0,0,0,51,5,1,0,0,0,52,53,3,2,1,0,53,54,5,17,0,0,54,55,
        3,8,4,0,55,60,3,18,9,0,56,57,5,16,0,0,57,59,3,18,9,0,58,56,1,0,0,
        0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,86,1,0,0,0,62,60,
        1,0,0,0,63,64,3,2,1,0,64,65,5,17,0,0,65,66,3,10,5,0,66,71,3,18,9,
        0,67,68,5,16,0,0,68,70,3,18,9,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,
        1,0,0,0,71,72,1,0,0,0,72,86,1,0,0,0,73,71,1,0,0,0,74,75,3,2,1,0,
        75,76,5,17,0,0,76,77,3,12,6,0,77,82,3,18,9,0,78,79,5,16,0,0,79,81,
        3,18,9,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,
        83,86,1,0,0,0,84,82,1,0,0,0,85,52,1,0,0,0,85,63,1,0,0,0,85,74,1,
        0,0,0,86,7,1,0,0,0,87,88,7,0,0,0,88,9,1,0,0,0,89,90,5,10,0,0,90,
        91,5,18,0,0,91,92,5,22,0,0,92,98,5,19,0,0,93,94,5,11,0,0,94,95,5,
        18,0,0,95,96,5,22,0,0,96,98,5,19,0,0,97,89,1,0,0,0,97,93,1,0,0,0,
        98,11,1,0,0,0,99,100,7,1,0,0,100,13,1,0,0,0,101,102,3,12,6,0,102,
        103,5,18,0,0,103,104,5,22,0,0,104,105,5,19,0,0,105,15,1,0,0,0,106,
        107,5,21,0,0,107,108,5,20,0,0,108,109,5,21,0,0,109,17,1,0,0,0,110,
        111,5,18,0,0,111,112,5,21,0,0,112,113,5,16,0,0,113,114,3,2,1,0,114,
        115,5,19,0,0,115,123,1,0,0,0,116,117,5,18,0,0,117,118,3,16,8,0,118,
        119,5,16,0,0,119,120,3,2,1,0,120,121,5,19,0,0,121,123,1,0,0,0,122,
        110,1,0,0,0,122,116,1,0,0,0,123,19,1,0,0,0,12,24,30,36,38,42,50,
        60,71,82,85,97,122
    ]

class AbstractMachineParser ( Parser ):

    grammarFileName = "AbstractMachineParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.DATA'", "'STACK'", "'QUEUE'", "'TAPE'", 
                     "'.LOGIC'", "'SCAN'", "'PRINT'", "'SCAN RIGHT'", "'SCAN LEFT'", 
                     "'READ'", "'WRITE'", "'RIGHT'", "'LEFT'", "'UP'", "'DOWN'", 
                     "','", "']'", "'('", "')'", "'/'" ]

    symbolicNames = [ "<INVALID>", "DATA", "STACK", "QUEUE", "TAPE", "LOGIC", 
                      "SCAN", "PRINT", "SCAN_RIGHT", "SCAN_LEFT", "READ", 
                      "WRITE", "RIGHT", "LEFT", "UP", "DOWN", "COMMA", "CLOSE_BRACKET", 
                      "OPEN_PAR", "CLOSE_PAR", "SLASH", "SYMBOL", "IDENTIFIER", 
                      "WS" ]

    RULE_program = 0
    RULE_identifer = 1
    RULE_memory_declaration = 2
    RULE_logic_declaration = 3
    RULE_commmand = 4
    RULE_memory_operation = 5
    RULE_direction = 6
    RULE_move_over_tape = 7
    RULE_replacement = 8
    RULE_param_list = 9

    ruleNames =  [ "program", "identifer", "memory_declaration", "logic_declaration", 
                   "commmand", "memory_operation", "direction", "move_over_tape", 
                   "replacement", "param_list" ]

    EOF = Token.EOF
    DATA=1
    STACK=2
    QUEUE=3
    TAPE=4
    LOGIC=5
    SCAN=6
    PRINT=7
    SCAN_RIGHT=8
    SCAN_LEFT=9
    READ=10
    WRITE=11
    RIGHT=12
    LEFT=13
    UP=14
    DOWN=15
    COMMA=16
    CLOSE_BRACKET=17
    OPEN_PAR=18
    CLOSE_PAR=19
    SLASH=20
    SYMBOL=21
    IDENTIFIER=22
    WS=23

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

        def DATA(self):
            return self.getToken(AbstractMachineParser.DATA, 0)

        def LOGIC(self):
            return self.getToken(AbstractMachineParser.LOGIC, 0)

        def memory_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.Memory_declarationContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.Memory_declarationContext,i)


        def logic_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.Logic_declarationContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.Logic_declarationContext,i)


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AbstractMachineParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(AbstractMachineParser.DATA)
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 21
                    self.memory_declaration()
                    self.state = 24 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                        break

                self.state = 26
                self.match(AbstractMachineParser.LOGIC)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 27
                    self.logic_declaration()
                    self.state = 30 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==21 or _la==22):
                        break

                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(AbstractMachineParser.LOGIC)
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 33
                    self.logic_declaration()
                    self.state = 36 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==21 or _la==22):
                        break

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


    class IdentiferContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_identifer

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SymbolAsIdentifierContext(IdentiferContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.IdentiferContext
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


    class IdentifierContext(IdentiferContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.IdentiferContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)



    def identifer(self):

        localctx = AbstractMachineParser.IdentiferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_identifer)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = AbstractMachineParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            elif token in [21]:
                localctx = AbstractMachineParser.SymbolAsIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
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


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_memory_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class QueueDeclarationContext(Memory_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.Memory_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUEUE(self):
            return self.getToken(AbstractMachineParser.QUEUE, 0)
        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueueDeclaration" ):
                listener.enterQueueDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueueDeclaration" ):
                listener.exitQueueDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueueDeclaration" ):
                return visitor.visitQueueDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class TapeDeclarationContext(Memory_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.Memory_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAPE(self):
            return self.getToken(AbstractMachineParser.TAPE, 0)
        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTapeDeclaration" ):
                listener.enterTapeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTapeDeclaration" ):
                listener.exitTapeDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTapeDeclaration" ):
                return visitor.visitTapeDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class StackDeclarationContext(Memory_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AbstractMachineParser.Memory_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STACK(self):
            return self.getToken(AbstractMachineParser.STACK, 0)
        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStackDeclaration" ):
                listener.enterStackDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStackDeclaration" ):
                listener.exitStackDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStackDeclaration" ):
                return visitor.visitStackDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def memory_declaration(self):

        localctx = AbstractMachineParser.Memory_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memory_declaration)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = AbstractMachineParser.StackDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(AbstractMachineParser.STACK)
                self.state = 45
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            elif token in [3]:
                localctx = AbstractMachineParser.QueueDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(AbstractMachineParser.QUEUE)
                self.state = 47
                self.match(AbstractMachineParser.IDENTIFIER)
                pass
            elif token in [4]:
                localctx = AbstractMachineParser.TapeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(AbstractMachineParser.TAPE)
                self.state = 49
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

        def identifer(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentiferContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(AbstractMachineParser.CLOSE_BRACKET, 0)

        def commmand(self):
            return self.getTypedRuleContext(AbstractMachineParser.CommmandContext,0)


        def param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AbstractMachineParser.Param_listContext)
            else:
                return self.getTypedRuleContext(AbstractMachineParser.Param_listContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AbstractMachineParser.COMMA)
            else:
                return self.getToken(AbstractMachineParser.COMMA, i)

        def memory_operation(self):
            return self.getTypedRuleContext(AbstractMachineParser.Memory_operationContext,0)


        def direction(self):
            return self.getTypedRuleContext(AbstractMachineParser.DirectionContext,0)


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_logic_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_declaration" ):
                listener.enterLogic_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_declaration" ):
                listener.exitLogic_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_declaration" ):
                return visitor.visitLogic_declaration(self)
            else:
                return visitor.visitChildren(self)




    def logic_declaration(self):

        localctx = AbstractMachineParser.Logic_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_logic_declaration)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.identifer()
                self.state = 53
                self.match(AbstractMachineParser.CLOSE_BRACKET)
                self.state = 54
                self.commmand()
                self.state = 55
                self.param_list()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 56
                    self.match(AbstractMachineParser.COMMA)
                    self.state = 57
                    self.param_list()
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.identifer()
                self.state = 64
                self.match(AbstractMachineParser.CLOSE_BRACKET)
                self.state = 65
                self.memory_operation()
                self.state = 66
                self.param_list()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 67
                    self.match(AbstractMachineParser.COMMA)
                    self.state = 68
                    self.param_list()
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.identifer()
                self.state = 75
                self.match(AbstractMachineParser.CLOSE_BRACKET)
                self.state = 76
                self.direction()
                self.state = 77
                self.param_list()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 78
                    self.match(AbstractMachineParser.COMMA)
                    self.state = 79
                    self.param_list()
                    self.state = 84
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


    class CommmandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCAN(self):
            return self.getToken(AbstractMachineParser.SCAN, 0)

        def PRINT(self):
            return self.getToken(AbstractMachineParser.PRINT, 0)

        def SCAN_RIGHT(self):
            return self.getToken(AbstractMachineParser.SCAN_RIGHT, 0)

        def SCAN_LEFT(self):
            return self.getToken(AbstractMachineParser.SCAN_LEFT, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_commmand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommmand" ):
                listener.enterCommmand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommmand" ):
                listener.exitCommmand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommmand" ):
                return visitor.visitCommmand(self)
            else:
                return visitor.visitChildren(self)




    def commmand(self):

        localctx = AbstractMachineParser.CommmandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_commmand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(AbstractMachineParser.READ)
                self.state = 90
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 91
                self.match(AbstractMachineParser.IDENTIFIER)
                self.state = 92
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(AbstractMachineParser.WRITE)
                self.state = 94
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 95
                self.match(AbstractMachineParser.IDENTIFIER)
                self.state = 96
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


    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RIGHT(self):
            return self.getToken(AbstractMachineParser.RIGHT, 0)

        def LEFT(self):
            return self.getToken(AbstractMachineParser.LEFT, 0)

        def UP(self):
            return self.getToken(AbstractMachineParser.UP, 0)

        def DOWN(self):
            return self.getToken(AbstractMachineParser.DOWN, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirection" ):
                listener.enterDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirection" ):
                listener.exitDirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirection" ):
                return visitor.visitDirection(self)
            else:
                return visitor.visitChildren(self)




    def direction(self):

        localctx = AbstractMachineParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_direction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Move_over_tapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def direction(self):
            return self.getTypedRuleContext(AbstractMachineParser.DirectionContext,0)


        def OPEN_PAR(self):
            return self.getToken(AbstractMachineParser.OPEN_PAR, 0)

        def IDENTIFIER(self):
            return self.getToken(AbstractMachineParser.IDENTIFIER, 0)

        def CLOSE_PAR(self):
            return self.getToken(AbstractMachineParser.CLOSE_PAR, 0)

        def getRuleIndex(self):
            return AbstractMachineParser.RULE_move_over_tape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove_over_tape" ):
                listener.enterMove_over_tape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove_over_tape" ):
                listener.exitMove_over_tape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMove_over_tape" ):
                return visitor.visitMove_over_tape(self)
            else:
                return visitor.visitChildren(self)




    def move_over_tape(self):

        localctx = AbstractMachineParser.Move_over_tapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_move_over_tape)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.direction()
            self.state = 102
            self.match(AbstractMachineParser.OPEN_PAR)
            self.state = 103
            self.match(AbstractMachineParser.IDENTIFIER)
            self.state = 104
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

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(AbstractMachineParser.SYMBOL)
            else:
                return self.getToken(AbstractMachineParser.SYMBOL, i)

        def SLASH(self):
            return self.getToken(AbstractMachineParser.SLASH, 0)

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
            self.state = 106
            self.match(AbstractMachineParser.SYMBOL)
            self.state = 107
            self.match(AbstractMachineParser.SLASH)
            self.state = 108
            self.match(AbstractMachineParser.SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
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

        def identifer(self):
            return self.getTypedRuleContext(AbstractMachineParser.IdentiferContext,0)


        def CLOSE_PAR(self):
            return self.getToken(AbstractMachineParser.CLOSE_PAR, 0)

        def replacement(self):
            return self.getTypedRuleContext(AbstractMachineParser.ReplacementContext,0)


        def getRuleIndex(self):
            return AbstractMachineParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = AbstractMachineParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 111
                self.match(AbstractMachineParser.SYMBOL)
                self.state = 112
                self.match(AbstractMachineParser.COMMA)
                self.state = 113
                self.identifer()
                self.state = 114
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(AbstractMachineParser.OPEN_PAR)
                self.state = 117
                self.replacement()
                self.state = 118
                self.match(AbstractMachineParser.COMMA)
                self.state = 119
                self.identifer()
                self.state = 120
                self.match(AbstractMachineParser.CLOSE_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





