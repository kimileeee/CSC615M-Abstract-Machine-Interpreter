from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from model.Memory import Stack, Queue, Tape1D, Tape2D
from tabulate import tabulate
from model.AbstractMachineUtils import AbstractMachineUtils

class AbstractMachineModel():
    def __init__(self):
        self.machine_initial = None
        self.data_memory = {}
        self.states = {}
        self.transitions = {}
        self.start_state = None
        self.is_two_way = False

        # For tape input
        self.input_tape = None
        
        # For running the machine
        self.input_string = ""
        self.pointer = 0
        self.current_state = None
        self.history = []

    def reset(self):
        self.data_memory = self.machine_initial.data_memory
        self.states = self.machine_initial.states
        self.transitions = self.machine_initial.transitions
        self.start_state = self.machine_initial.start_state
        self.is_two_way = self.machine_initial.is_two_way
        self.input_tape = self.machine_initial.input_tape
        self.input_string = self.machine_initial.input_string
        self.pointer = self.machine_initial.pointer
        self.current_state = self.machine_initial.current_state
        self.history = self.machine_initial.history

    # GETTERS AND SETTERS
    def add_data_memory(self, name, value=None):
        if name in self.data_memory:
            raise Exception("Memory {} already declared".format(name))
        self.data_memory[name] = value

    def get_data_memory(self, name):
        if name in self.data_memory:
            return self.data_memory[name]
        raise Exception("Memory {} not found".format(name))
    
    def get_start_state(self):
        return self.start_state
    
    def set_start_state(self, state):
        if self.start_state is None:
            self.start_state = state
    
    def get_input_tape(self):
        return self.input_tape
    
    def set_input_tape(self, tape):
        if self.input_tape is None:
            self.input_tape = tape

    def is_memory_empty(self):
        return all(mem.is_empty() for mem in self.data_memory.values())
        
    # DISPLAY/PRINT METHODS
    def __str__(self):
        return f"\nData Memory: {self.data_memory}\nStart State: {self.start_state}\nStates: {self.states}\nTransitions: {self.transitions}\nIs Two Way: {self.is_two_way}\n"

    def print_machine(self):
        self.print_memory()
        self.print_states()
        self.print_transitions()

    def print_memory(self):
        print("\nMemory")
        print(tabulate([(k, type(v).__name__, v) for k, v in self.data_memory.items()], 
               headers=["Memory", "Type", "Value"], 
               tablefmt="pretty"))
        
    def print_states(self):
        print("\nStates")
        print(tabulate(self.states.items(), headers=["State", "Command"], tablefmt="pretty"))

        print("\nStart State: ", self.start_state)

    def print_transitions(self):
        print("\nTransitions")
        symbols = sorted({symbol for state in self.transitions.values() for symbol in state})
        table_data = []
        try:
            table_data = [[state] + [", ".join(sorted(self.transitions[state].get(symbol, set()))) or "-" for symbol in symbols]
                        for state in self.transitions]
        except:
            table_data = [[s] + [", ".join(f"({out}, {ns})" for out, ns in self.transitions[s].get(sym, set())) or "-" for sym in symbols] for s in self.transitions]

        print(tabulate(table_data, headers=["State"] + symbols, tablefmt="pretty"))


    # MACHINE OPERATIONS
    
    def initialize(self, input_string):
        if self.input_tape:
            self.input_tape.initialize_input(input_string)
        
        input_string = "#" + input_string + "#"
        self.pointer = 0

        self.input_string = input_string
        self.current_state = self.start_state
        self.history = []
        print("Status:")
        print(self.get_status())
        print()
        return self.get_status()
    
    def get_status(self):
        return {
            "current_state": self.current_state,
            "pointer": self.pointer,
            "input_string": self.input_string,
            "history": list(self.history)
        }

    def next_step(self):        
        # Save current state for potential rollback.
        self.history.append((self.current_state, self.pointer, self.input_string))
        
        # Execute the new state's action using our reusable method.
        symbol = self.execute_action(self.current_state)
        
        print(self)

        # Print the overall status.
        status = f"State: {self.current_state}, Pointer: {self.pointer}, Input: {self.input_string}"
        print(status)
        # Lookup possible transitions.
        print(f"Symbol: {symbol}\n")
        state_transitions = self.transitions.get(self.current_state, {})
        possible = state_transitions.get(symbol)
        if not possible:
            # TODO: if deterministic, should return rejected here, but if nondeterministic, should stop exploring this path
            # return f"Error: No transition from state {self.current_state} on symbol '{symbol}'."
            self.current_state = AbstractMachineUtils.REJECT
            return f"REJECTED"
        
        # Choose a transition (for nondeterminism, extend as needed).
        next_transition = next(iter(possible))
        replacement = None
        if isinstance(next_transition, tuple):
            replacement, next_state = next_transition
            # Replace the symbol on the tape.
            self.input_string = (
                self.input_string[:self.pointer] +
                replacement +
                self.input_string[self.pointer+1:]
            )
        else:
            next_state = next_transition
        
        # Update the current state.
        self.current_state = next_state
        
        # Check if we have reached the accepting state.
        if self.current_state == AbstractMachineUtils.ACCEPT:
            # Save current (final) state to history.
            self.history.append((self.current_state, self.pointer, self.input_string))
            return f"ACCEPTED"
        elif self.current_state == AbstractMachineUtils.REJECT:
            # Save current (final) state to history.
            self.history.append((self.current_state, self.pointer, self.input_string))
            return f"REJECTED"
        
        return status
    
    def next_step_nda(self):
        # Save current state set for potential rollback.
        self.history.append((set(self.active_states), self.pointer, self.input_string))

        new_active_states = set()

        for state in self.active_states:
            # Execute the new state's action using our reusable method.
            symbol = self.execute_action(state)
            print(f"Processing state: {state} with symbol: {symbol}")

            # Lookup possible transitions for this state.
            state_transitions = self.transitions.get(state, {})
            possible_next_states = state_transitions.get(symbol, set())

            if not possible_next_states:
                continue  # No valid transition from this state

            new_active_states.update(possible_next_states)

        if not new_active_states:
            # If no new states are active, the machine has rejected the input.
            self.active_states = {AbstractMachineUtils.REJECT}
            return "REJECTED"

        self.active_states = new_active_states

        # Check if any active state reaches the accept state
        if AbstractMachineUtils.ACCEPT in self.active_states:
            return "ACCEPTED"

        # Log the current active states
        return f"Active States: {self.active_states}, Pointer: {self.pointer}, Input: {self.input_string}"

        

    def prev_step(self):
        """
        Rolls back the simulation to the previous state.
        """
        if not self.history:
            return "No previous state."
        self.current_state, self.pointer, self.input_string = self.history.pop()
        return f"(Rewind) State: {self.current_state}, Pointer: {self.pointer}, Input: {self.input_string}"

    def execute_action(self, state):
        """
        Execute the action associated with the given state.
        Updates the pointer and/or data_memory as needed.
        Returns a log message for the action.
        """
        action = self.states.get(state)
        symbol = "#"
        log = f">> State {state} Action: {action}"
        if action:
            # ----- INPUT OPERATIONS -----
            if action.startswith(AbstractMachineUtils.SCAN_LEFT):
                self.pointer = max(0, self.pointer - 1)
                symbol = self.input_string[self.pointer]
                log += f"\nTwo-Way: Scanned left to symbol '{symbol}'"
            elif action.startswith(AbstractMachineUtils.SCAN_RIGHT):
                self.pointer += 1
                if self.pointer < len(self.input_string):
                    symbol = self.input_string[self.pointer]
                    log += f"\nTwo-Way: Scanned right to symbol '{symbol}'"
            elif action.startswith(AbstractMachineUtils.SCAN):
                self.pointer += 1
                if self.pointer < len(self.input_string):
                    symbol = self.input_string[self.pointer]
                    log += f"\nOne-Way: Scanned symbol '{symbol}'"
            
            # ----- PRINT OPERATIONS -----
            elif action.startswith(AbstractMachineUtils.PRINT):
                # Assume output is handled elsewhere; here we log the output.
                symbol = next(iter(self.transitions[state]))
                log += f"\nState {state} Action: {action} -> Writing '{symbol}'"
            
            # ----- MEMORY OPERATIONS -----
            elif action.startswith(AbstractMachineUtils.READ):
                identifier = action.split("(")[1].rstrip(")")
                memory = self.data_memory[identifier]
                if memory:
                    if isinstance(memory, Stack):
                        symbol = memory.pop()
                    elif isinstance(memory, Queue):
                        symbol = memory.dequeue()
                    log += f"\nState {state} Action: {action} -> Read '{symbol}' from {identifier}"
                else:
                    log += f"\nState {state} Action: {action} -> Memory '{identifier}' is empty!"
            elif action.startswith(AbstractMachineUtils.WRITE):
                identifier = action.split("(")[1].rstrip(")")
                memory = self.data_memory[identifier]
                symbol = next(iter(self.transitions[state]))
                if isinstance(memory, Stack):
                    memory.push(symbol)
                elif isinstance(memory, Queue):
                    memory.enqueue(symbol)
                log += f"\nState {state} Action: {action} -> Writing '{symbol}' to {identifier}"
            
            # ----- Turing Machine Specific Operations -----
            elif action.startswith(AbstractMachineUtils.LEFT):
                identifier = action.split("(")[1].rstrip(")")
                memory = self.data_memory[identifier]
                symbol = next(iter(self.transitions[state]))
                # Assume transition returns a tuple: (replacement, next_state)
                replace = list(self.transitions[state][symbol])[0][0]
                if memory and memory.get_left() == symbol:
                    memory.move_left(replace)
                    log += f"\nState {state} Action: {action} -> Moving left on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move left on tape '{identifier}'"
            elif action.startswith(AbstractMachineUtils.RIGHT):
                identifier = action.split("(")[1].rstrip(")")
                memory = self.data_memory[identifier]
                symbol = next(iter(self.transitions[state]))
                replace = list(self.transitions[state][symbol])[0][0]
                if memory and memory.get_right() == symbol:
                    print(f"Replacing {memory.get_right()} with {replace}")
                    memory.move_right(replace)
                    log += f"\nState {state} Action: {action} -> Moving right on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move right on tape '{identifier}'"
            elif action.startswith(AbstractMachineUtils.UP):
                identifier = action.split("(")[1].rstrip(")")
                memory = self.data_memory[identifier]
                symbol = next(iter(self.transitions[state]))
                replace = list(self.transitions[state][symbol])[0][0]
                if memory and memory.get_up() == symbol:
                    memory.move_up(replace)
                    log += f"\nState {state} Action: {action} -> Moving up on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move up on tape '{identifier}'"
            elif action.startswith(AbstractMachineUtils.DOWN):
                identifier = action.split("(")[1].rstrip(")")
                memory = self.data_memory[identifier]
                symbol = next(iter(self.transitions[state]))
                replace = list(self.transitions[state][symbol])[0][0]
                if memory and memory.get_down() == symbol:
                    memory.move_down(replace)
                    log += f"\nState {state} Action: {action} -> Moving down on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move down on tape '{identifier}'"
        print(log)
        return symbol