from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor
from model.Memory import Stack, Queue, Tape1D, Tape2D
from model.AbstractMachineUtils import AbstractMachineUtils
from model.AbstractMachineModel import AbstractMachineModel
import copy

class AbstractMachineInterpreter(AbstractMachineParserVisitor):

    def __init__(self):
        super(AbstractMachineParserVisitor, self).__init__()
        self.machine = AbstractMachineModel()

    # VISITOR METHODS
    ## START
    def visitFullProgram(self, ctx:AbstractMachineParser.FullProgramContext):
        self.visitChildren(ctx)
        
        self.machine.machine_initial = copy.deepcopy(self.machine)
        print(self.machine)
        self.machine.print_machine()

    ## MEMORY DECLARATION
    def visitMemory_declaration(self, ctx:AbstractMachineParser.Memory_declarationContext):
        identifier = ctx.IDENTIFIER().getText()

        if ctx.STACK():
            self.machine.add_data_memory(identifier, Stack())
        elif ctx.QUEUE():
            self.machine.add_data_memory(identifier, Queue())
        elif ctx.TAPE():
            tape = Tape1D()
            self.machine.add_data_memory(identifier, tape)
            self.machine.set_input_tape(tape)
        elif ctx.TAPE_2D():
            tape = Tape2D()
            self.machine.add_data_memory(identifier, tape)
            self.machine.set_input_tape(tape)

        self.visitChildren(ctx)
    
    ## LOGIC DECLARATIONS
    def visitCommandLogicDeclaration(self, ctx:AbstractMachineParser.CommandLogicDeclarationContext):
        # print ("in command logic declaration")
        state_identifier = ctx.identifier().getText()
        
        self.machine.set_start_state(state_identifier)

        command = ctx.command().getText()
        self.machine.states[state_identifier] = command

        # print(f"State {state_identifier} Command: {command}")
        
        if command in [AbstractMachineUtils.SCAN_LEFT, AbstractMachineUtils.SCAN_RIGHT]:
            self.machine.is_two_way = True

        for i in ctx.transition():
            self.visitTransition(state_identifier, i)

        for state in self.machine.states:
            if state not in self.machine.transitions:
                self.machine.transitions[state] = {}

    def visitMemoryOperationLogicDeclaration(self, ctx:AbstractMachineParser.MemoryOperationLogicDeclarationContext):
        # print ("in read write logic declaration")
        state_identifier = ctx.identifier().getText()
        
        self.machine.set_start_state(state_identifier)

        command = ctx.memory_operation().getText()
        self.machine.states[state_identifier] = command
        
        for i in ctx.transition():
            self.visitTransition(state_identifier, i)

        for state in self.machine.states:
            if state not in self.machine.transitions:
                self.machine.transitions[state] = {}

    def visitMoveOverTapeLogicDeclaration(self, ctx:AbstractMachineParser.MoveOverTapeLogicDeclarationContext):
        # print ("in tape logic declaration")
        state_identifier = ctx.identifier().getText()

        self.machine.set_start_state(state_identifier)

        command = ctx.tape_operation().getText()
        self.machine.states[state_identifier] = command
        
        for i in ctx.replacement():
            self.visitReplacement(state_identifier, i)

        for state in self.machine.states:
            if state not in self.machine.transitions:
                self.machine.transitions[state] = {}
    
    def visitTransition(self, curr_state, ctx:AbstractMachineParser.TransitionContext):
        symbol = ctx.SYMBOL().getText()
        next_state = ctx.identifier().getText()

        if curr_state not in self.machine.transitions:
            self.machine.transitions[curr_state] = {}

        if symbol not in self.machine.transitions[curr_state]:
            self.machine.transitions[curr_state][symbol] = set()
        self.machine.transitions[curr_state][symbol].add(next_state)

        # If the next state is "accept" or "reject", ensure it is recorded
        if next_state in [AbstractMachineUtils.ACCEPT, AbstractMachineUtils.REJECT]:
            self.machine.states[next_state] = None

        # print(f"Added transition: {curr_state} --({symbol})--> {next_state}")

    def visitReplacement(self, curr_state, ctx:AbstractMachineParser.ReplacementContext):
        symbol = ctx.SYMBOL()[0].getText()
        symbol_replace = ctx.SYMBOL()[1].getText()
        next_state = ctx.identifier().getText()

        if curr_state not in self.machine.transitions:
            self.machine.transitions[curr_state] = {}

        if symbol not in self.machine.transitions[curr_state]:
            self.machine.transitions[curr_state][symbol] = set()
        self.machine.transitions[curr_state][symbol].add((symbol_replace, next_state))

        # If the next state is "accept" or "reject", ensure it is recorded
        if next_state in [AbstractMachineUtils.ACCEPT, AbstractMachineUtils.REJECT]:
            self.machine.states[next_state] = None

        # print(f"Added transition: {curr_state} --({symbol})--> replace with {symbol_replace}, {next_state}")