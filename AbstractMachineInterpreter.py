from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor
from Memory import Stack, Queue, Tape1D, Tape2D
from tabulate import tabulate
from AbstractMachineGUI import AbstractMachineGUI

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
    ## Visualization DONE, need to fix self loops, text should be command, and add state name in box
    ## Input -> Output
    ## Step by Step
    ## Multiple Input Runs
    def run_gui(self):
        AbstractMachineGUI(self).run()

    def run_machine(self, input_string):
        print("Machine Type:", self.machine_type)
        print("States:", self.states)
        print("Start State:", self.start_state)
        print("Transitions:", self.transitions)
        print("Data Memory:", self.data_memory)
        print("Two-way:", self.is_two_way)
        print()

        if self.is_two_way:
            if self.machine_type == self.MACHINE_TYPE_FSM:
                self.run_fsm(input_string)
            elif self.machine_type == self.MACHINE_TYPE_FSA:
                self.run_fsa_two_way(input_string)
            elif self.machine_type == self.MACHINE_TYPE_PDA:
                self.run_pda_two_way(input_string)
            elif self.machine_type == self.MACHINE_TYPE_GST:
                self.run_gst_two_way(input_string)
            elif self.machine_type == self.MACHINE_TYPE_TURING:
                self.run_turing(input_string)
        else:
            if self.machine_type == self.MACHINE_TYPE_FSM:
                self.run_fsm(input_string)
            elif self.machine_type == self.MACHINE_TYPE_FSA:
                self.run_fsa_one_way(input_string)
            elif self.machine_type == self.MACHINE_TYPE_PDA:
                self.run_pda_one_way(input_string)
            elif self.machine_type == self.MACHINE_TYPE_GST:
                self.run_gst_one_way(input_string)
            elif self.machine_type == self.MACHINE_TYPE_TURING:
                self.run_turing(input_string)

    def run_fsm(self, input_string):
        print("Running FSM")
        active_states = {self.start_state}  # Start with the initial state
        input_pointer = 0
        output = ""

        while input_pointer < len(input_string):
            next_active_states = set()
            symbol = input_string[input_pointer]

            for state in active_states:
                command = self.states[state]

                if command in self.get_lexer_name(AbstractMachineParser.SCAN):
                    print(f"Reading Symbol: {symbol}")
                    input_pointer += 1

                elif command in self.get_lexer_name(AbstractMachineParser.PRINT):
                    output += symbol

                if state in self.transitions and symbol in self.transitions[state]:
                    next_active_states.update(self.transitions[state][symbol])

            active_states = next_active_states

        print(f"Output: {output}")

    def run_fsa_one_way(self, input_string):
        print("Running FSA One-Way")
        active_states = {self.start_state}
        input_pointer = 0

        while input_pointer < len(input_string):
            next_active_states = set()
            symbol = input_string[input_pointer]

            for state in active_states:
                command = self.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS
                    if command in self.get_lexer_name(AbstractMachineParser.SCAN):
                        print(f"Reading Symbol: {symbol}")
                        input_pointer += 1
                    
                    elif command in self.get_lexer_name(AbstractMachineParser.SCAN_RIGHT):
                        input_pointer += 1
                        symbol = input_string[input_pointer]
                        print(f"Reading Symbol: {symbol}")

                    elif command in self.get_lexer_name(AbstractMachineParser.SCAN_LEFT):
                        input_pointer -= 1
                        if input_pointer >= 0:
                            symbol = input_string[input_pointer]
                            print(f"Reading Symbol: {symbol}")

                    # PRINT OPERATIONS
                    elif command in self.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.transitions[state]))
                        output += symbol

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"State {state} Action: {command} -> Read '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Stack {identifier} is empty!")
                            print(f"Data Memory: {self.data_memory}")
                    
                    elif self.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]
                        symbol = next(iter(self.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.transitions and symbol in self.transitions[state]:
                    next_active_states.update(self.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            if not bool(active_states):
                break

        print(f"\nFinal Active States: {active_states}")
        if self.ACCEPT in active_states:
            print("\nInput accepted!")
            return True
        else:
            print("\nInput rejected!")
            return False

    def run_fsa_two_way(self, input_string):
        print("Running FSA Two-Way")
        active_states = {self.start_state}
        input_pointer = 0
        input_string = "#" + input_string + "#"

        while input_pointer < len(input_string):
            next_active_states = set()
            symbol = input_string[input_pointer]

            for state in active_states:
                command = self.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS                    
                    if command in self.get_lexer_name(AbstractMachineParser.SCAN_RIGHT):
                        input_pointer += 1
                        symbol = input_string[input_pointer]
                        print(f"Reading Symbol: {symbol}")

                    elif command in self.get_lexer_name(AbstractMachineParser.SCAN_LEFT):
                        input_pointer -= 1
                        if input_pointer >= 0:
                            symbol = input_string[input_pointer]
                            print(f"Reading Symbol: {symbol}")

                    # PRINT OPERATIONS
                    elif command in self.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.transitions[state]))
                        output += symbol

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"State {state} Action: {command} -> Read '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Stack {identifier} is empty!")
                            print(f"Data Memory: {self.data_memory}")
                    
                    elif self.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]
                        symbol = next(iter(self.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.transitions and symbol in self.transitions[state]:
                    next_active_states.update(self.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            print(f"Input Pointer: {input_pointer}, Input Length: {len(input_string)}")

            if self.ACCEPT in active_states:
                print("\nInput accepted!")
                return True
            
            if not bool(active_states): # No more next states
                break

        print(f"\nFinal Active States: {active_states}")
        if self.ACCEPT in active_states:
            print("\nInput accepted!")
            return True
        else:
            print("\nInput rejected!")
            return False

    def run_pda_one_way(self, input_string):
        print("Running PDA One-Way")
        active_states = {self.start_state}
        input_pointer = 0

        input_string = input_string + "#"

        while input_pointer < len(input_string) or not self.is_memory_empty():
            next_active_states = set()
            if input_pointer < len(input_string):
                symbol = input_string[input_pointer]

            for state in active_states:
                command = self.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS
                    if command in self.get_lexer_name(AbstractMachineParser.SCAN):
                        print(f"Scanning Symbol: {symbol}")
                        input_pointer += 1

                    # PRINT OPERATIONS
                    elif command in self.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.transitions[state]))
                        output += symbol

                        print(f"Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"Reading '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.data_memory}")
                        else:
                            print(f"Reading, stack {identifier} is empty!")
                            print(f"Data Memory: {self.data_memory}")
                    
                    elif self.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]
                        symbol = next(iter(self.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.transitions and symbol in self.transitions[state]:
                    next_active_states.update(self.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            print(f"Is Memory Empty: {self.is_memory_empty()}")
            if not bool(active_states):
                break

        print(f"\nFinal Active States: {active_states}")
        if self.ACCEPT in active_states:
            print("\nInput accepted!")
            return True
        else:
            print("\nInput rejected!")
            return False
    
    def run_pda_two_way(self, input_string):
        print("Running PDA Two-Way")
        active_states = {self.start_state}
        input_pointer = 0

        input_string = "#" + input_string + "#"

        while input_pointer < len(input_string) or not self.is_memory_empty():
            next_active_states = set()
            if input_pointer < len(input_string):
                symbol = input_string[input_pointer]

            for state in active_states:
                command = self.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS
                    if command in self.get_lexer_name(AbstractMachineParser.SCAN_RIGHT):
                        input_pointer += 1
                        symbol = input_string[input_pointer]
                        print(f"Reading Symbol: {symbol}")

                    elif command in self.get_lexer_name(AbstractMachineParser.SCAN_LEFT):
                        input_pointer -= 1
                        if input_pointer >= 0:
                            symbol = input_string[input_pointer]
                            print(f"Reading Symbol: {symbol}")

                    # PRINT OPERATIONS
                    elif command in self.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.transitions[state]))
                        output += symbol

                        print(f"Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"Reading '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.data_memory}")
                        else:
                            print(f"Reading, stack {identifier} is empty!")
                            print(f"Data Memory: {self.data_memory}")
                    
                    elif self.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.data_memory[identifier]
                        symbol = next(iter(self.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.transitions and symbol in self.transitions[state]:
                    next_active_states.update(self.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            print(f"Is Memory Empty: {self.is_memory_empty()}")

            if self.ACCEPT in active_states:
                print("\nInput accepted!")
                return True
            
            if not bool(active_states):
                break

        print(f"\nFinal Active States: {active_states}")
        if self.ACCEPT in active_states:
            print("\nInput accepted!")
            return True
        else:
            print("\nInput rejected!")
            return False

    # TODO: Implement these methods
    def run_gst_one_way(self, input_string):
        print("Running GST One-Way")

    def run_gst_two_way(self, input_string):
        print("Running GST Two-Way")

    def run_turing(self, input_string):
        print("Running Turing Machine")


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