from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from automata.AbstractMachineParserVisitor import AbstractMachineParserVisitor
from Memory import Stack, Queue, Tape1D, Tape2D
from tabulate import tabulate
from AbstractMachineGUI import AbstractMachineGUI

class AbstractMachineRunner():
    def __init__(self, machine):
        self.machine = machine

    def run_machine(self, input_string: str) -> str:
        """
        Generalized machine runner that supports one-way and two-way execution.
        It also stores all transition paths taken in a dictionary.
        
        Parameters:
        input_string: The input string to be processed.
        two_way: If True, the machine will run in two-way mode (with left/right scanning)
                and the input string is padded with '#' at both ends.
                If False, the machine is assumed to run one-way.
        
        Returns:
        A string indicating whether the input was accepted or rejected.
        """

        # Initialize output (used for PRINT operations) and the dictionary for recording paths.
        output = ""
        transition_paths = {}  # key: iteration number, value: list of transition dicts
        iteration = 0
        two_way = self.machine.is_two_way

        # Adjust the input string based on whether the machine is two-way.
        # For two-way machines, add boundary markers at both ends.
        if two_way:
            input_string = "#" + input_string + "#"
        else:
            # For some machines (like PDAs) you might want to signal end-of-input.
            # If the machine supports memory (e.g., has an is_memory_empty method), append an end marker.
            if hasattr(self.machine, "is_memory_empty"):
                input_string = input_string + "#"
        
        # Set the initial pointer and active states.
        input_pointer = 0
        active_states = {self.machine.start_state}
        
        # Determine the loop condition: if the machine uses memory (like PDAs or Turing)
        # then we continue while either there is more input OR memory is not empty.
        def continue_loop():
            if hasattr(self.machine, "is_memory_empty"):
                return input_pointer < len(input_string) or not self.machine.is_memory_empty()
            return input_pointer < len(input_string)
        
        # Main loop: process the input string (and possibly memory) until no further transitions.
        while continue_loop():
            # For this iteration, record all transitions.
            transition_paths[iteration] = []
            next_active_states = set()
            
            # Fetch the current symbol if available.
            symbol = input_string[input_pointer] if input_pointer < len(input_string) else None
            
            # Process each active state.
            for state in active_states:
                command = self.machine.states[state]
                # Record a snapshot for this state
                step_info = {
                    "from_state": state,
                    "command": command,
                    "input_pointer": input_pointer,
                    "read_symbol": symbol,
                    "to_states": []
                }
                print(f"\nProcessing State: {state} with Command: {command}")

                if command:
                    # ----- INPUT OPERATIONS -----
                    # For two-way machines, use SCAN_RIGHT and SCAN_LEFT commands.\
                    if self.machine.get_lexer_name(AbstractMachineParser.SCAN_RIGHT) in command:
                        input_pointer += 1
                        if input_pointer < len(input_string):
                            symbol = input_string[input_pointer]
                        print(f"Two-Way: Scanned right to symbol '{symbol}'")
                    elif self.machine.get_lexer_name(AbstractMachineParser.SCAN_LEFT) in command:
                        input_pointer = max(0, input_pointer - 1)
                        symbol = input_string[input_pointer]
                        print(f"Two-Way: Scanned left to symbol '{symbol}'")
                    elif command == self.machine.get_lexer_name(AbstractMachineParser.SCAN):
                        print(f"One-Way: Scanned symbol '{symbol}'")
                        input_pointer += 1
                        if input_pointer < len(input_string):
                            symbol = input_string[input_pointer]\
                    
                    # ----- PRINT OPERATIONS -----
                    elif self.machine.get_lexer_name(AbstractMachineParser.PRINT) in command:
                        # Assume transitions for print operations have at least one symbol.
                        next_symbol = next(iter(self.machine.transitions[state]))
                        output += next_symbol
                        print(f"State {state} Action: {command} -> Writing '{next_symbol}'")
                    
                    # ----- MEMORY OPERATIONS -----
                    elif self.machine.get_lexer_name(AbstractMachineParser.READ) in command:
                        # Expected format: READ(identifier)
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        if memory:
                            if isinstance(memory, Stack):
                                symbol = memory.pop()
                            elif isinstance(memory, Queue):
                                symbol = memory.dequeue()
                            print(f"State {state} Action: {command} -> Read '{symbol}' from {identifier}")
                        else:
                            print(f"State {state} Action: {command} -> Memory '{identifier}' is empty!")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.WRITE) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        # Again, assume there is at least one symbol in the transition table.
                        next_symbol = next(iter(self.machine.transitions[state]))
                        if isinstance(memory, Stack):
                            memory.push(next_symbol)
                        elif isinstance(memory, Queue):
                            memory.enqueue(next_symbol)
                        print(f"State {state} Action: {command} -> Writing '{next_symbol}' to {identifier}")
                    
                    # ----- Turing Machine Specific Operations -----
                    # (Left, Right, Up, Down) commands are processed similarly to two-way scanning,
                    # but include an extra step of replacing the symbol.
                    elif self.machine.get_lexer_name(AbstractMachineParser.LEFT) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        next_symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][next_symbol][0] if self.machine.transitions[state][next_symbol][0] else None
                        if memory:
                            memory.move_left(next_symbol, replace)
                            print(f"State {state} Action: {command} -> Moving left on tape '{identifier}'")
                        else:
                            print(f"State {state} Action: {command} -> Tape '{identifier}' is empty!")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.RIGHT) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        next_symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][next_symbol][0] if self.machine.transitions[state][next_symbol][0] else None
                        if memory:
                            memory.move_right(next_symbol, replace)
                            print(f"State {state} Action: {command} -> Moving right on tape '{identifier}'")
                        else:
                            print(f"State {state} Action: {command} -> Tape '{identifier}' is empty!")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.UP) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        next_symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][next_symbol][0] if self.machine.transitions[state][next_symbol][0] else None
                        if memory:
                            memory.move_up(next_symbol, replace)
                            print(f"State {state} Action: {command} -> Moving up on tape '{identifier}'")
                        else:
                            print(f"State {state} Action: {command} -> Tape '{identifier}' is empty!")
                    
                    elif self.machine.get_lexer_name(AbstractMachineParser.DOWN) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]
                        next_symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][next_symbol][0] if self.machine.transitions[state][next_symbol][0] else None
                        if memory:
                            memory.move_down(next_symbol, replace)
                            print(f"State {state} Action: {command} -> Moving down on tape '{identifier}'")
                        else:
                            print(f"State {state} Action: {command} -> Tape '{identifier}' is empty!")
                
                # End of command processing for the current state.
                # If there is a valid transition on the current symbol, add those states.
                if state in self.machine.transitions and symbol in self.machine.transitions[state]:
                    destinations = self.machine.transitions[state][symbol]
                    next_active_states.update(destinations)
                    # Record each transition for this state.
                    for dest in destinations:
                        step_info["to_states"].append(dest)
                
                # Save the step info for this state in the current iteration.
                transition_paths[iteration].append(step_info)
            
            active_states = next_active_states
            print(f"Iteration {iteration}: Next active states: {active_states}")
            iteration += 1
            
            # For two-way machines (and Turing/PDA), we can check for early acceptance.
            if self.machine.ACCEPT in active_states:
                print(f"Accepted at iteration {iteration} with states: {active_states}")
                # Optionally, you can store the final transition info as well.
                return "\nInput accepted!"
            
            # If no states are active, break out.
            if not active_states:
                break

        print(f"\nFinal Active States: {active_states}")
        # After processing, decide acceptance.
        if self.machine.ACCEPT in active_states:
            result = "\nInput accepted!"
        else:
            result = "\nInput rejected!"
        
        # For debugging or later use, the entire transition_paths dict can be inspected.
        # For example: print(transition_paths) or store it as an attribute.
        self.transition_paths = transition_paths

        print(f"\nTransition Paths: {transition_paths}")

        return result


    def run(self, input_string):
        print("Machine Type:", self.machine.machine_type)
        print("States:", self.machine.states)
        print("Start State:", self.machine.start_state)
        print("Transitions:", self.machine.transitions)
        print("Data Memory:", self.machine.data_memory)
        print("Two-way:", self.machine.is_two_way)
        print()

        result = None

        if self.machine.is_two_way:
            if self.machine.machine_type == self.machine.MACHINE_TYPE_FSM:
                result = self.run_fsm(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_FSA:
                result = self.run_fsa_two_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_PDA:
                result = self.run_pda_two_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_GST:
                result = self.run_gst_two_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_TURING:
                result = self.run_turing(input_string)
        else:
            if self.machine.machine_type == self.machine.MACHINE_TYPE_FSM:
                result = self.run_fsm(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_FSA:
                result = self.run_fsa_one_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_PDA:
                result = self.run_pda_one_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_GST:
                result = self.run_gst_one_way(input_string)
            elif self.machine.machine_type == self.machine.MACHINE_TYPE_TURING:
                result = self.run_turing(input_string)

        return result


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
        else:
            return "\nInput rejected!"

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
        else:
            return "\nInput rejected!"

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
        active_states = {self.machine.start_state}
        input_pointer = 0

        input_string = "#" + input_string + "#"

        # TODO: Put input string on first tape in memory

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
                    
                    # Turing Machine Commands
                    elif self.machine.get_lexer_name(AbstractMachineParser.LEFT) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][symbol][0] if self.machine.transitions[state][symbol][0] else None

                        if memory:
                            memory.move_left(symbol, replace)
                            print(f"State {state} Action: {command} -> Moving left to {identifier}, replacing {symbol} with {replace}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Tape {identifier} is empty!")
                            print(f"Data Memory: {self.machine.data_memory}")

                    elif self.machine.get_lexer_name(AbstractMachineParser.RIGHT) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][symbol][0] if self.machine.transitions[state][symbol][0] else None

                        if memory:
                            memory.move_right(symbol, replace)
                            print(f"State {state} Action: {command} -> Moving right to {identifier}, replacing {symbol} with {replace}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Tape {identifier} is empty!")
                            print(f"Data Memory: {self.machine.data_memory}")

                    elif self.machine.get_lexer_name(AbstractMachineParser.UP) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][symbol][0] if self.machine.transitions[state][symbol][0] else None

                        if memory:
                            memory.move_up(symbol, replace)
                            print(f"State {state} Action: {command} -> Moving up to {identifier}, replacing {symbol} with {replace}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Tape {identifier} is empty!")
                            print(f"Data Memory: {self.machine.data_memory}")

                    elif self.machine.get_lexer_name(AbstractMachineParser.DOWN) in command:
                        identifier = command.split("(")[1].rstrip(")")
                        memory = self.machine.data_memory[identifier]

                        symbol = next(iter(self.machine.transitions[state]))
                        replace = self.machine.transitions[state][symbol][0] if self.machine.transitions[state][symbol][0] else None

                        if memory:
                            memory.move_down(symbol, replace)
                            print(f"State {state} Action: {command} -> Moving down to {identifier}, replacing {symbol} with {replace}")
                            print(f"Data Memory: {self.machine.data_memory}")
                        else:
                            print(f"State {state} Action: {command} -> Tape {identifier} is empty!")
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
        else:
            return "\nInput rejected!"
        