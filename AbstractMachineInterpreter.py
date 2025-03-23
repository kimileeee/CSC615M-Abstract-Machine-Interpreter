from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor
from Memory import Stack, Queue, Tape1D, Tape2D
from tabulate import tabulate
from AbstractMachineGUI import AbstractMachineGUI
from AbstractMachineRunner import AbstractMachineRunner

class AbstractMachineInterpreter(AbstractMachineParserVisitor):

    ACCEPT = "accept"
    REJECT = "reject"

    MACHINE_TYPE_FSM = "fsm"            # SCAN, PRINT
    MACHINE_TYPE_FSA = "fsa"            # SCAN, ACCEPT/REJECT
    MACHINE_TYPE_PDA = "pda"            # SCAN, READ, WRITE, ACCEPT/REJECT
    MACHINE_TYPE_GST = "gst"            # SCAN, PRINT, READ, WRITE
    MACHINE_TYPE_TURING = "turing"      # LEFT, RIGHT, UP, DOWN

    def __init__(self):
        super(AbstractMachineParserVisitor, self).__init__()
        self.data_memory = {}
        self.states = {}
        self.transitions = {}
        self.start_state = None
        self.is_two_way = False
        self.machine_type = None

        self.accept_states = []
        self.reject_states = []

        self.input_symbols = {}
        self.input_tape = None

    # TODO: Implement GUI
    ## Visualization of states DONE, 
    # need to fix self loops, text should be command, and add state name in box
    ## Visualization of memory
    ## Input -> Output
    ## Step by Step
    ## Multiple Input Runs
    def run_gui(self):
        AbstractMachineGUI(self).run()

    def run_machine(self, input_string):
        runner = AbstractMachineRunner(self)
        return runner.run_machine(input_string)

    ########
    def get_lexer_name(self, index):
        return AbstractMachineLexer.literalNames[index].strip("'")

    # DATA MEMORY TABLE OPERATIONS
    def declare_data_memory(self, name, value=None):
        if name in self.data_memory:
            raise Exception("Memory {} already declared".format(name))
        self.data_memory[name] = value

    def get_data_memory(self, name):
        if name in self.data_memory:
            return self.data_memory[name]
        raise Exception("Memory {} not found".format(name))

    def print_machine(self):
        print("\nMemory")
        print(tabulate([(k, type(v).__name__, v) for k, v in self.data_memory.items()], 
               headers=["Memory", "Type", "Value"], 
               tablefmt="pretty"))

        print("\nStates")
        print(tabulate(self.states.items(), headers=["State", "Command"], tablefmt="pretty"))

        print("\nStart State: ", self.start_state)

        print("\nTransitions")
        symbols = sorted({symbol for state in self.transitions.values() for symbol in state})
        table_data = []
        try:
            table_data = [[state] + [", ".join(sorted(self.transitions[state].get(symbol, set()))) or "-" for symbol in symbols]
                        for state in self.transitions]
        except:
            table_data = [[s] + [", ".join(f"({out}, {ns})" for out, ns in self.transitions[s].get(sym, set())) or "-" for sym in symbols] for s in self.transitions]

        print(tabulate(table_data, headers=["State"] + symbols, tablefmt="pretty"))

    def set_machine_type(self):
        if any((isinstance(memory, Tape1D) or isinstance(memory, Tape2D)) for memory in self.data_memory.values()):
            self.machine_type = self.MACHINE_TYPE_TURING
        elif self.data_memory: # Has memory but no tape
            if any(state in [self.ACCEPT, self.REJECT] for state in self.states):
                self.machine_type = self.MACHINE_TYPE_PDA
            else:
                self.machine_type = self.MACHINE_TYPE_GST
        else: # No memory, finite state machine
            if any(state in [self.ACCEPT, self.REJECT] for state in self.states):
                self.machine_type = self.MACHINE_TYPE_FSA
            else:
                self.machine_type = self.MACHINE_TYPE_FSM

    def is_memory_empty(self):
        return all(mem.is_empty() for mem in self.data_memory.values())
    
    # VISITOR METHODS
    ## START
    def visitFullProgram(self, ctx:AbstractMachineParser.FullProgramContext):
        for i in ctx.children:
            print(i.getText())
        print()

        self.visitChildren(ctx)
        print(self.transitions)
        self.set_machine_type()
        self.print_machine()

    ## MEMORY DECLARATION
    def visitMemory_declaration(self, ctx:AbstractMachineParser.Memory_declarationContext):
        identifier = ctx.IDENTIFIER().getText()

        if ctx.STACK():
            self.declare_data_memory(identifier, Stack())
        elif ctx.QUEUE():
            self.declare_data_memory(identifier, Queue())
        elif ctx.TAPE():
            tape = Tape1D()
            self.declare_data_memory(identifier, tape)
            if self.input_tape is None:
                self.input_tape = tape
        elif ctx.TAPE_2D():
            tape = Tape2D()
            self.declare_data_memory(identifier, tape)
            if self.input_tape is None:
                self.input_tape = tape

        self.visitChildren(ctx)
    
    ## LOGIC DECLARATIONS
    def visitCommandLogicDeclaration(self, ctx:AbstractMachineParser.CommandLogicDeclarationContext):
        print ("in command logic declaration")
        state_identifier = ctx.identifier().getText()
        if self.start_state is None:
            self.start_state = state_identifier

        command = ctx.command().getText()
        self.states[state_identifier] = command

        print(f"State {state_identifier} Command: {command}")
        
        if command in [self.get_lexer_name(AbstractMachineParser.SCAN_LEFT), 
                       self.get_lexer_name(AbstractMachineParser.SCAN_RIGHT)]:
            self.is_two_way = True

        for i in ctx.transition():
            self.visitTransition(state_identifier, i)

        for state in self.states:
            if state not in self.transitions:
                self.transitions[state] = {}

    def visitMemoryOperationLogicDeclaration(self, ctx:AbstractMachineParser.MemoryOperationLogicDeclarationContext):
        print ("in read write logic declaration")
        state_identifier = ctx.identifier().getText()
        if self.start_state is None:
            self.start_state = state_identifier

        command = ctx.memory_operation().getText()
        self.states[state_identifier] = command
        
        for i in ctx.transition():
            self.visitTransition(state_identifier, i)

        for state in self.states:
            if state not in self.transitions:
                self.transitions[state] = {}

    def visitMoveOverTapeLogicDeclaration(self, ctx:AbstractMachineParser.MoveOverTapeLogicDeclarationContext):
        print ("in tape logic declaration")
        state_identifier = ctx.identifier().getText()

        if self.start_state is None:
            self.start_state = state_identifier

        command = ctx.tape_operation().getText()
        self.states[state_identifier] = command
        
        for i in ctx.replacement():
            self.visitReplacement(state_identifier, i)

        for state in self.states:
            if state not in self.transitions:
                self.transitions[state] = {}
    
    def visitTransition(self, curr_state, ctx:AbstractMachineParser.TransitionContext):
        symbol = ctx.SYMBOL().getText()
        next_state = ctx.identifier().getText()

        if curr_state not in self.transitions:
            self.transitions[curr_state] = {}

        if symbol not in self.transitions[curr_state]:
            self.transitions[curr_state][symbol] = set()
        self.transitions[curr_state][symbol].add(next_state)

        # If the next state is "accept" or "reject", ensure it is recorded
        if next_state in [self.ACCEPT, self.REJECT]:
            self.states[next_state] = None

        # print(f"Added transition: {curr_state} --({symbol})--> {next_state}")

    def visitReplacement(self, curr_state, ctx:AbstractMachineParser.ReplacementContext):
        symbol = ctx.SYMBOL()[0].getText()
        symbol_replace = ctx.SYMBOL()[1].getText()
        next_state = ctx.identifier().getText()

        if curr_state not in self.transitions:
            self.transitions[curr_state] = {}

        if symbol not in self.transitions[curr_state]:
            self.transitions[curr_state][symbol] = set()
        self.transitions[curr_state][symbol].add((symbol_replace, next_state))

        # If the next state is "accept" or "reject", ensure it is recorded
        if next_state in [self.ACCEPT, self.REJECT]:
            self.states[next_state] = None

        # print(f"Added transition: {curr_state} --({symbol})--> replace with {symbol_replace}, {next_state}")