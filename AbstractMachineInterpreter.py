from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor
from Memory import Stack, Queue, Tape1D, Tape2D
from tabulate import tabulate

class AbstractMachineInterpreter(AbstractMachineParserVisitor):

    ACCEPT = "accept"
    REJECT = "reject"

    def __init__(self):
        super(AbstractMachineParserVisitor, self).__init__()
        self.data_memory = {}
        self.states = {}
        self.transitions = {}
        self.start_state = None
        self.is_two_way = False

        self.accept_states = []
        self.reject_states = []

        self.input_symbols = {}
        self.input_tape = None

    def run_machine(self, input_string):
        print("Data Memory:", self.data_memory)
        print("States:", self.states)
        print("Transitions:", self.transitions)
        print("Start State:", self.start_state)
        
        active_states = {self.start_state}  # Start with the initial state
        current_state = self.start_state
        input_pointer = 0

        if self.is_two_way:
            input_string = "#" + input_string + "#"

        print(f"Input: {input_string}")
        print(f"Start State: {current_state}")

        # while current_state not in [self.ACCEPT, self.REJECT]:
        while active_states: 

            if self.is_two_way:
                pass
            else:
                if input_pointer == len(input_string):
                    if self.ACCEPT in active_states:
                        print("\nInput accepted!")
                        return True
                    else:
                        print("\nInput rejected!")
                        return False
            
            next_active_states = set()
        
            for state in active_states:
                # Perform the state's action
                print()
                if self.states[state]:
                    command = self.states[state]

                    # INPUT OPERATIONS
                    if command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.SCAN]:
                        symbol = input_string[input_pointer]
                        print(f"Reading Symbol: {symbol}")
                        input_pointer += 1

                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.SCAN_RIGHT]:
                        input_pointer += 1
                        symbol = input_string[input_pointer] if input_pointer < len(input_string) else "#"
                        print(f"Reading Symbol: {symbol}")

                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.SCAN_LEFT]:
                        input_pointer -= 1
                        if input_pointer >= 0:
                            symbol = input_string[input_pointer] if input_pointer < len(input_string) else "#"
                            print(f"Reading Symbol: {symbol}")


                    # PRINT OPERATIONS
                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.PRINT]:
                        pass
                    
                    # MEMORY OPERATIONS
                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.READ]:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            elif isinstance(memory, Tape1D):
                                symbol = memory.read()
                            elif isinstance(memory, Tape2D):
                                symbol = memory.read()
                            print(f"State {state} Action: {command} -> Read '{symbol}' from {identifier}")
                        else:
                            print(f"State {state} Action: {command} -> Stack {identifier} is empty!")
                    
                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.WRITE]:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)
                        elif isinstance(memory, Tape1D):
                            memory.write(symbol)
                        elif isinstance(memory, Tape2D):
                            memory.write(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                    
                    # TAPE OPERATIONS
                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.LEFT]:
                        pass
                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.RIGHT]:
                        pass
                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.UP]:
                        pass
                    elif command in AbstractMachineLexer.symbolicNames[AbstractMachineParser.DOWN]:
                        pass

                # Determine possible next states
                print(f"Current State: {state}")
                print(f"Symbol: {symbol}")
                if state in self.transitions and symbol in self.transitions[state]:
                    transition_set = self.transitions[state][symbol]
                    print(f"Transition set: {transition_set}")
                    if transition_set and isinstance(next(iter(transition_set)), tuple):
                        for symbol_replace, next_state in transition_set:
                            next_active_states.add(next_state)
                    else:
                        next_active_states.update(transition_set)

            # Move to the next set of active states
            active_states = next_active_states

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

    # VISITOR METHODS
    ## START
    def visitFullProgram(self, ctx:AbstractMachineParser.FullProgramContext):
        for i in ctx.children:
            print(i.getText())
        print()

        self.visitChildren(ctx)
        print(self.transitions)
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

        if command in [AbstractMachineLexer.symbolicNames[AbstractMachineParser.SCAN_LEFT],
                       AbstractMachineLexer.symbolicNames[AbstractMachineParser.SCAN_RIGHT]]:
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