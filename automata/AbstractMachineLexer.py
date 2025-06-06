# Generated from ./automata/AbstractMachineLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,25,190,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,
        19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,5,22,166,8,22,10,22,12,22,
        169,9,22,1,23,1,23,1,23,1,23,5,23,175,8,23,10,23,12,23,178,9,23,
        1,23,1,23,1,23,1,23,1,24,4,24,185,8,24,11,24,12,24,186,1,24,1,24,
        1,176,0,25,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,1,0,4,4,0,35,36,48,57,65,90,97,122,2,0,65,90,97,122,
        4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,192,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,
        23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,
        33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,
        43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,1,51,1,0,0,0,3,
        57,1,0,0,0,5,63,1,0,0,0,7,69,1,0,0,0,9,74,1,0,0,0,11,82,1,0,0,0,
        13,89,1,0,0,0,15,94,1,0,0,0,17,100,1,0,0,0,19,111,1,0,0,0,21,121,
        1,0,0,0,23,126,1,0,0,0,25,132,1,0,0,0,27,138,1,0,0,0,29,143,1,0,
        0,0,31,146,1,0,0,0,33,151,1,0,0,0,35,153,1,0,0,0,37,155,1,0,0,0,
        39,157,1,0,0,0,41,159,1,0,0,0,43,161,1,0,0,0,45,163,1,0,0,0,47,170,
        1,0,0,0,49,184,1,0,0,0,51,52,5,46,0,0,52,53,5,68,0,0,53,54,5,65,
        0,0,54,55,5,84,0,0,55,56,5,65,0,0,56,2,1,0,0,0,57,58,5,83,0,0,58,
        59,5,84,0,0,59,60,5,65,0,0,60,61,5,67,0,0,61,62,5,75,0,0,62,4,1,
        0,0,0,63,64,5,81,0,0,64,65,5,85,0,0,65,66,5,69,0,0,66,67,5,85,0,
        0,67,68,5,69,0,0,68,6,1,0,0,0,69,70,5,84,0,0,70,71,5,65,0,0,71,72,
        5,80,0,0,72,73,5,69,0,0,73,8,1,0,0,0,74,75,5,50,0,0,75,76,5,68,0,
        0,76,77,5,95,0,0,77,78,5,84,0,0,78,79,5,65,0,0,79,80,5,80,0,0,80,
        81,5,69,0,0,81,10,1,0,0,0,82,83,5,46,0,0,83,84,5,76,0,0,84,85,5,
        79,0,0,85,86,5,71,0,0,86,87,5,73,0,0,87,88,5,67,0,0,88,12,1,0,0,
        0,89,90,5,83,0,0,90,91,5,67,0,0,91,92,5,65,0,0,92,93,5,78,0,0,93,
        14,1,0,0,0,94,95,5,80,0,0,95,96,5,82,0,0,96,97,5,73,0,0,97,98,5,
        78,0,0,98,99,5,84,0,0,99,16,1,0,0,0,100,101,5,83,0,0,101,102,5,67,
        0,0,102,103,5,65,0,0,103,104,5,78,0,0,104,105,5,32,0,0,105,106,5,
        82,0,0,106,107,5,73,0,0,107,108,5,71,0,0,108,109,5,72,0,0,109,110,
        5,84,0,0,110,18,1,0,0,0,111,112,5,83,0,0,112,113,5,67,0,0,113,114,
        5,65,0,0,114,115,5,78,0,0,115,116,5,32,0,0,116,117,5,76,0,0,117,
        118,5,69,0,0,118,119,5,70,0,0,119,120,5,84,0,0,120,20,1,0,0,0,121,
        122,5,82,0,0,122,123,5,69,0,0,123,124,5,65,0,0,124,125,5,68,0,0,
        125,22,1,0,0,0,126,127,5,87,0,0,127,128,5,82,0,0,128,129,5,73,0,
        0,129,130,5,84,0,0,130,131,5,69,0,0,131,24,1,0,0,0,132,133,5,82,
        0,0,133,134,5,73,0,0,134,135,5,71,0,0,135,136,5,72,0,0,136,137,5,
        84,0,0,137,26,1,0,0,0,138,139,5,76,0,0,139,140,5,69,0,0,140,141,
        5,70,0,0,141,142,5,84,0,0,142,28,1,0,0,0,143,144,5,85,0,0,144,145,
        5,80,0,0,145,30,1,0,0,0,146,147,5,68,0,0,147,148,5,79,0,0,148,149,
        5,87,0,0,149,150,5,78,0,0,150,32,1,0,0,0,151,152,5,44,0,0,152,34,
        1,0,0,0,153,154,5,93,0,0,154,36,1,0,0,0,155,156,5,40,0,0,156,38,
        1,0,0,0,157,158,5,41,0,0,158,40,1,0,0,0,159,160,5,47,0,0,160,42,
        1,0,0,0,161,162,7,0,0,0,162,44,1,0,0,0,163,167,7,1,0,0,164,166,7,
        2,0,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,
        0,0,0,168,46,1,0,0,0,169,167,1,0,0,0,170,171,5,47,0,0,171,172,5,
        47,0,0,172,176,1,0,0,0,173,175,9,0,0,0,174,173,1,0,0,0,175,178,1,
        0,0,0,176,177,1,0,0,0,176,174,1,0,0,0,177,179,1,0,0,0,178,176,1,
        0,0,0,179,180,5,10,0,0,180,181,1,0,0,0,181,182,6,23,0,0,182,48,1,
        0,0,0,183,185,7,3,0,0,184,183,1,0,0,0,185,186,1,0,0,0,186,184,1,
        0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,189,6,24,0,0,189,50,1,
        0,0,0,4,0,167,176,186,1,6,0,0
    ]

class AbstractMachineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ERRORS = 2

    DATA = 1
    STACK = 2
    QUEUE = 3
    TAPE = 4
    TAPE_2D = 5
    LOGIC = 6
    SCAN = 7
    PRINT = 8
    SCAN_RIGHT = 9
    SCAN_LEFT = 10
    READ = 11
    WRITE = 12
    RIGHT = 13
    LEFT = 14
    UP = 15
    DOWN = 16
    COMMA = 17
    CLOSE_BRACKET = 18
    OPEN_PAR = 19
    CLOSE_PAR = 20
    SLASH = 21
    SYMBOL = 22
    IDENTIFIER = 23
    COMMENT = 24
    WS = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"ERRORS" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.DATA'", "'STACK'", "'QUEUE'", "'TAPE'", "'2D_TAPE'", "'.LOGIC'", 
            "'SCAN'", "'PRINT'", "'SCAN RIGHT'", "'SCAN LEFT'", "'READ'", 
            "'WRITE'", "'RIGHT'", "'LEFT'", "'UP'", "'DOWN'", "','", "']'", 
            "'('", "')'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "DATA", "STACK", "QUEUE", "TAPE", "TAPE_2D", "LOGIC", "SCAN", 
            "PRINT", "SCAN_RIGHT", "SCAN_LEFT", "READ", "WRITE", "RIGHT", 
            "LEFT", "UP", "DOWN", "COMMA", "CLOSE_BRACKET", "OPEN_PAR", 
            "CLOSE_PAR", "SLASH", "SYMBOL", "IDENTIFIER", "COMMENT", "WS" ]

    ruleNames = [ "DATA", "STACK", "QUEUE", "TAPE", "TAPE_2D", "LOGIC", 
                  "SCAN", "PRINT", "SCAN_RIGHT", "SCAN_LEFT", "READ", "WRITE", 
                  "RIGHT", "LEFT", "UP", "DOWN", "COMMA", "CLOSE_BRACKET", 
                  "OPEN_PAR", "CLOSE_PAR", "SLASH", "SYMBOL", "IDENTIFIER", 
                  "COMMENT", "WS" ]

    grammarFileName = "AbstractMachineLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


