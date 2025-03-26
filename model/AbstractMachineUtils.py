from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser

class AbstractMachineUtils:
    
    @staticmethod
    def get_lexer_name(index):
        return AbstractMachineLexer.literalNames[index].strip("'")

    ACCEPT = "accept"
    REJECT = "reject"
    SCAN = get_lexer_name(AbstractMachineParser.SCAN)
    SCAN_LEFT = get_lexer_name(AbstractMachineParser.SCAN_LEFT)
    SCAN_RIGHT = get_lexer_name(AbstractMachineParser.SCAN_RIGHT)
    PRINT = get_lexer_name(AbstractMachineParser.PRINT)
    READ = get_lexer_name(AbstractMachineParser.READ)
    WRITE = get_lexer_name(AbstractMachineParser.WRITE)
    LEFT = get_lexer_name(AbstractMachineParser.LEFT)
    RIGHT = get_lexer_name(AbstractMachineParser.RIGHT)
    UP = get_lexer_name(AbstractMachineParser.UP)
    DOWN = get_lexer_name(AbstractMachineParser.DOWN)

    shorthand_actions = {
        SCAN: "S",
        SCAN_LEFT: "SL",
        SCAN_RIGHT: "SR",
        PRINT: "P",
        READ: "Rd",
        WRITE: "Wr",
        LEFT: "L",
        RIGHT: "R",
        UP: "U",
        DOWN: "D"
    }