from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor

class AbstractMachineInterpreter(AbstractMachineParserVisitor):

    def __init__(self):
        super(AbstractMachineParserVisitor, self).__init__()
        self.symbol_table = [{}]

    # SYMBOL TABLE OPERATIONS
    def enter_scope(self):
        self.symbol_table.append({})

    def exit_scope(self):
        self.symbol_table.pop()

    def declare_symbol(self, name, value=None, type=None):
        if name in self.symbol_table[-1]:
            raise Exception("Symbol {} already declared".format(name))
        self.symbol_table[-1][name] = {'value': value, 'type': type}

    def assign_symbol(self, name, value):
        for scope in reversed(self.symbol_table):
            if name in scope:
                scope[name]['value'] = value
                return
            
        raise Exception("Symbol {} not declared".format(name))

    def lookup_symbol(self, name):
        for scope in reversed(self.symbol_table):
            if name in scope:
                return scope[name]
        raise Exception("Symbol {} not found".format(name))
    
    def print_symbol_table(self):
        print("\nSymbol Table:")
        for i, scope in enumerate(self.symbol_table):
            print(f"Scope {i}: {scope}")
        print() 

    # VISITOR METHODS
    def visitProgram(self, ctx:AbstractMachineParser.ProgramContext):
        pass

        return self.visitChildren(ctx)
    

    def visitStackDeclaration(self, ctx:AbstractMachineParser.StackDeclarationContext):
        identifier = ctx.IDENTIFIER().getText()
        self.declare_symbol(identifier, type='stack')

        return self.visitChildren(ctx)

    def visitQueueDeclaration(self, ctx:AbstractMachineParser.QueueDeclarationContext):
        identifier = ctx.IDENTIFIER().getText()
        self.declare_symbol(identifier, type='queue')

        return self.visitChildren(ctx)

    def visitTapeDeclaration(self, ctx:AbstractMachineParser.TapeDeclarationContext):
        identifier = ctx.IDENTIFIER().getText()
        self.declare_symbol(identifier, type='tape')

        return self.visitChildren(ctx)