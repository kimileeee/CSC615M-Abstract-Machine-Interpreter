from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor
from Memory import Stack, Queue, Tape1D, Tape2D
from tabulate import tabulate
from AbstractMachineGUI import AbstractMachineGUI

class AbstractMachineRunner():
    def __init__(self, machine):
        self.machine = machine

    def run(self, input_string):
        print("Machine Type:", self.machine.machine_type)
        print("States:", self.machine.states)
        print("Start State:", self.machine.start_state)
        print("Transitions:", self.machine.transitions)
        print("Data Memory:", self.machine.data_memory)
        print("Two-way:", self.machine.is_two_way)
        print()

        if self.machine.is_two_way:
            if self.machine.machine_type == self.machine.MACHINE_TYPE_FSM:
                self.run_fsm(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_FSA:
                self.run_fsa_two_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_PDA:
                self.run_pda_two_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_GST:
                self.run_gst_two_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_TURING:
                self.run_turing(input_string)
        else:
            if self.machine.machine_type == self.machine.MACHINE_TYPE_FSM:
                self.run_fsm(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_FSA:
                self.run_fsa_one_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_PDA:
                self.run_pda_one_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_GST:
                self.run_gst_one_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_TURING:
                self.run_turing(input_string)

    def run_fsm(self, input_string):
        print("Running FSM")
        active_states = {self.machine.start_state}  # Start with the initial state
        input_pointer = 0
        output = ""

        while input_pointer < len(input_string):
            next_active_states = set()
            symbol = input_string[input_pointer]

            for state in active_states:
                command = self.machine.states[state]

                if command in self.machine.get_lexer_name(AbstractMachineParser.SCAN):
                    print(f"Reading Symbol: {symbol}")
                    input_pointer += 1

                elif command in self.machine.get_lexer_name(AbstractMachineParser.PRINT):
                    output += symbol

                if state in self.machine.transitions and symbol in self.machine.transitions[state]:
                    next_active_states.update(self.machine.transitions[state][symbol])

            active_states = next_active_states

        return output

    def run_fsa_one_way(self, input_string):
        print("Running FSA One-Way")
        active_states = {self.machine.start_state}
        input_pointer = 0

        while input_pointer < len(input_string):
            next_active_states = set()
            symbol = input_string[input_pointer]

            for state in active_states:
                command = self.machine.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS
                    if command in self.machine.get_lexer_name(AbstractMachineParser.SCAN):
                        print(f"Reading Symbol: {symbol}")
                        input_pointer += 1
                    
                    elif command in self.machine.get_lexer_name(AbstractMachineParser.SCAN_RIGHT):
                        input_pointer += 1
                        symbol = input_string[input_pointer]
                        print(f"Reading Symbol: {symbol}")

                    elif command in self.machine.get_lexer_name(AbstractMachineParser.SCAN_LEFT):
                        input_pointer -= 1
                        if input_pointer >= 0:
                            symbol = input_string[input_pointer]
                            print(f"Reading Symbol: {symbol}")

                    # PRINT OPERATIONS
                    elif command in self.machine.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.machine.transitions[state]))
                        output += symbol

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.machine.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"State {state} Action: {command} -> Read '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Stack {identifier} is empty!")
                            print(f"Data Memory: {self.machine.data_memory}")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        symbol = next(iter(self.machine.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.machine.transitions and symbol in self.machine.transitions[state]:
                    next_active_states.update(self.machine.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            if not bool(active_states):
                break

        print(f"\nFinal Active States: {active_states}")
        if self.machine.ACCEPT in active_states:
            return "\nInput accepted!"
            return True
        else:
            return "\nInput rejected!"
            return False

    def run_fsa_two_way(self, input_string):
        print("Running FSA Two-Way")
        active_states = {self.machine.start_state}
        input_pointer = 0
        input_string = "#" + input_string + "#"

        while input_pointer < len(input_string):
            next_active_states = set()
            symbol = input_string[input_pointer]

            for state in active_states:
                command = self.machine.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS                    
                    if command in self.machine.get_lexer_name(AbstractMachineParser.SCAN_RIGHT):
                        input_pointer += 1
                        symbol = input_string[input_pointer]
                        print(f"Reading Symbol: {symbol}")

                    elif command in self.machine.get_lexer_name(AbstractMachineParser.SCAN_LEFT):
                        input_pointer -= 1
                        if input_pointer >= 0:
                            symbol = input_string[input_pointer]
                            print(f"Reading Symbol: {symbol}")

                    # PRINT OPERATIONS
                    elif command in self.machine.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.machine.transitions[state]))
                        output += symbol

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.machine.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"State {state} Action: {command} -> Read '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Stack {identifier} is empty!")
                            print(f"Data Memory: {self.machine.data_memory}")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        symbol = next(iter(self.machine.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.machine.transitions and symbol in self.machine.transitions[state]:
                    next_active_states.update(self.machine.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            print(f"Input Pointer: {input_pointer}, Input Length: {len(input_string)}")

            if self.machine.ACCEPT in active_states:
                return "\nInput accepted!"
                return True
            
            if not bool(active_states): # No more next states
                break

        print(f"\nFinal Active States: {active_states}")
        if self.machine.ACCEPT in active_states:
            return "\nInput accepted!"
            return True
        else:
            return "\nInput rejected!"
            return False

    def run_pda_one_way(self, input_string):
        print("Running PDA One-Way")
        active_states = {self.machine.start_state}
        input_pointer = 0

        input_string = input_string + "#"

        while input_pointer < len(input_string) or not self.machine.is_memory_empty():
            next_active_states = set()
            if input_pointer < len(input_string):
                symbol = input_string[input_pointer]

            for state in active_states:
                command = self.machine.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS
                    if command in self.machine.get_lexer_name(AbstractMachineParser.SCAN):
                        print(f"Scanning Symbol: {symbol}")
                        input_pointer += 1

                    # PRINT OPERATIONS
                    elif command in self.machine.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.machine.transitions[state]))
                        output += symbol

                        print(f"Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.machine.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"Reading '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"Reading, stack {identifier} is empty!")
                            print(f"Data Memory: {self.machine.data_memory}")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        symbol = next(iter(self.machine.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.machine.transitions and symbol in self.machine.transitions[state]:
                    next_active_states.update(self.machine.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            print(f"Is Memory Empty: {self.machine.is_memory_empty()}")
            if not bool(active_states):
                break

        print(f"\nFinal Active States: {active_states}")
        print(f"\nFinal Active States: {active_states}")
        if self.machine.ACCEPT in active_states:
            return "\nInput accepted!"
            return True
        else:
            return "\nInput rejected!"
            return False
    
    def run_pda_two_way(self, input_string):
        print("Running PDA Two-Way")
        active_states = {self.machine.start_state}
        input_pointer = 0

        input_string = "#" + input_string + "#"

        while input_pointer < len(input_string) or not self.machine.is_memory_empty():
            next_active_states = set()
            if input_pointer < len(input_string):
                symbol = input_string[input_pointer]

            for state in active_states:
                command = self.machine.states[state]

                print(f"\nCommand: {command}")

                if command:
                    # INPUT OPERATIONS
                    if command in self.machine.get_lexer_name(AbstractMachineParser.SCAN_RIGHT):
                        input_pointer += 1
                        symbol = input_string[input_pointer]
                        print(f"Reading Symbol: {symbol}")

                    elif command in self.machine.get_lexer_name(AbstractMachineParser.SCAN_LEFT):
                        input_pointer -= 1
                        if input_pointer >= 0:
                            symbol = input_string[input_pointer]
                            print(f"Reading Symbol: {symbol}")

                    # PRINT OPERATIONS
                    elif command in self.machine.get_lexer_name(AbstractMachineParser.PRINT):
                        symbol = next(iter(self.machine.transitions[state]))
                        output += symbol

                        print(f"Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")
                    
                    # MEMORY OPERATIONS
                    elif self.machine.get_lexer_name(AbstractMachineParser.READ) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"Reading '{symbol}' from {identifier}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"Reading, stack {identifier} is empty!")
                            print(f"Data Memory: {self.machine.data_memory}")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        symbol = next(iter(self.machine.transitions[state]))

                        if isinstance(memory, Stack):
                            memory.push(symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(symbol)

                        print(f"State {state} Action: {command} -> Writing '{symbol}' to {identifier}")
                        print(f"Data Memory: {self.machine.data_memory}")

                else: # command is none, meaning the state being processed is an accept or reject state
                    pass

                if state in self.machine.transitions and symbol in self.machine.transitions[state]:
                    next_active_states.update(self.machine.transitions[state][symbol])

            active_states = next_active_states
            print(f"Next Active States: {active_states}, {bool(active_states)}")
            print(f"Is Memory Empty: {self.machine.is_memory_empty()}")

            if self.machine.ACCEPT in active_states:
                return "\nInput accepted!"
                return True
            
            if not bool(active_states):
                break

        print(f"\nFinal Active States: {active_states}")
        if self.machine.ACCEPT in active_states:
            return "\nInput accepted!"
            return True
        else:
            return "\nInput rejected!"
            return False

    # TODO: Implement these methods
    def run_gst_one_way(self, input_string):
        print("Running GST One-Way")

    def run_gst_two_way(self, input_string):
        print("Running GST Two-Way")

    def run_turing(self, input_string):
        print("Running Turing Machine")
        