from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from model.Memory import Stack, Queue, Tape1D, Tape2D
from tabulate import tabulate
from model.AbstractMachineUtils import AbstractMachineUtils
import copy

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
        self.output_string = None
        self.pointer = 0
        self.current_state = None
        self.history = []
        self.nda_path = None

    def reset(self):
        self.data_memory = self.machine_initial.data_memory
        self.states = self.machine_initial.states
        self.transitions = self.machine_initial.transitions
        self.start_state = self.machine_initial.start_state
        self.is_two_way = self.machine_initial.is_two_way
        self.input_tape = self.machine_initial.input_tape
        self.input_string = ""
        self.output_string = None
        self.pointer = 0
        self.current_state = self.machine_initial.current_state
        self.history = []
        self.nda_path = None

    # GETTERS AND SETTERS
    def get_status(self):
        return {
            "current_state": self.current_state,
            "pointer": self.pointer,
            "input_string": self.input_string,
            "history": list(self.history)
        }
    
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
    
    def is_nondeterministic(self):
        for state, transitions_for_state in self.transitions.items():
            for symbol, next_states in transitions_for_state.items():
                if len(next_states) > 1:
                    return True
        return False
        
    # DISPLAY/PRINT METHODS
    def __str__(self):
        return f"\nData Memory: {self.data_memory}\nStart State: {self.start_state}\nStates: {self.states}\nTransitions: {self.transitions}\nIs Two Way: {self.is_two_way}\n"

    def print_machine(self):
        self.print_memory()
        self.print_states()
        print("Non-deterministic: ", self.is_nondeterministic())
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

        if self.is_nondeterministic():
            self.nda_path = self.run_nondeterministic()
            print(f"Accepted ND Path: {self.nda_path}")
            if self.nda_path:
                self.nda_path.pop(0)

        return self.get_status()
    
    def run_nondeterministic(self):
        initial_config = (
            self.current_state, self.pointer, self.input_string,
            copy.deepcopy(self.data_memory), self.output_string, []
        )
        stack = [initial_config]
        
        while stack:
            cur_state, cur_ptr, cur_input, cur_memory, cur_output, cur_path = stack.pop()
            
            # If reached an accept state and finished scanning the input, return the path.
            # TBH not sure sa pointer part hskjdhf
            if cur_state == AbstractMachineUtils.ACCEPT and cur_ptr >= len(cur_input) - 2:
                return cur_path + [(cur_state, cur_ptr, cur_input, cur_memory, cur_output)]
            if cur_state == AbstractMachineUtils.REJECT:
                continue
            
            # Valid pointer
            if cur_ptr < 0 or cur_ptr >= len(cur_input):
                continue
            
            symbol, new_ptr, new_input, new_memory, new_output = self.execute_action(cur_state, cur_ptr, cur_input, cur_memory, cur_output)
            state_transitions = self.transitions.get(cur_state, {})
            possible_transitions = state_transitions.get(symbol)
            
            if not possible_transitions:
                continue  # dead state
            
            for next_transition in possible_transitions:
                new_state = None
                new_memory = copy.deepcopy(new_memory)

                if isinstance(next_transition, tuple):
                    replacement, ns = next_transition
                    new_state = ns
                    new_input = new_input[:new_ptr] + replacement + new_input[new_ptr+1:]
                else:
                    new_state = next_transition
                
                new_history = cur_path + [(cur_state, cur_ptr, cur_input, cur_memory, cur_output)]
                stack.append((new_state, new_ptr, new_input, new_memory, new_output, new_history))
        return None


    def next_step(self):        
        # Save current state for rollback
        self.history.append((self.current_state, self.pointer, self.input_string))
        
        symbol, self.pointer, self.input_string, self.data_memory, self.output_string = self.execute_action(self.current_state, self.pointer, self.input_string, self.data_memory, self.output_string)
        # print(self)

        # Print the overall status
        status = f"State: {self.current_state}, Pointer: {self.pointer}, Input: {self.input_string}"

        state_transitions = self.transitions.get(self.current_state, {})
        possible = state_transitions.get(symbol)
        if not possible:
            self.current_state = AbstractMachineUtils.REJECT
            if self.output_string is None:
                return f"REJECTED"
            else:
                return self.output_string
            
        # Choose a transition for nondeterministic machine
        nda_path = None
        if self.nda_path:
            next_nda, next_ptr, next_input, next_memory, next_output = self.nda_path.pop(0)

        next_transition = next(iter(possible))
        if nda_path and len(possible) > 1:
            try:
                next_transition = next_nda
                print(f"Choosing transition: {next_transition} from {possible}")
            except:
                return "REJECTED"
            
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
        
        # Update the current state
        self.current_state = next_state
        
        # Check if halting state (accept/reject)
        if self.current_state == AbstractMachineUtils.ACCEPT:
            self.history.append((self.current_state, self.pointer, self.input_string))
            if self.output_string is None:
                return f"ACCEPTED"
            else:
                return self.output_string
        elif self.current_state == AbstractMachineUtils.REJECT:
            self.history.append((self.current_state, self.pointer, self.input_string))
            if self.output_string is None:
                return f"REJECTED"
            else:
                return self.output_string
        
        # return status
    

    def prev_step(self):
        if not self.history:
            return "No previous state."
        self.current_state, self.pointer, self.input_string = self.history.pop()
        return f"(Rewind) State: {self.current_state}, Pointer: {self.pointer}, Input: {self.input_string}"


    def execute_action(self, state, pointer, input_string, data_memory, output_string):
        action = self.states.get(state)
        symbol = "#"
        log = f">> State {state} Action: {action}"
        if action:
            # ----- INPUT OPERATIONS -----
            if action.startswith(AbstractMachineUtils.SCAN_LEFT):
                pointer = max(0, pointer - 1)
                symbol = input_string[pointer]
                log += f"\nTwo-Way: Scanned left to symbol '{symbol}'"
            
            elif action.startswith(AbstractMachineUtils.SCAN_RIGHT):
                pointer += 1
                if pointer < len(input_string):
                    symbol = input_string[pointer]
                    log += f"\nTwo-Way: Scanned right to symbol '{symbol}'"
            
            elif action.startswith(AbstractMachineUtils.SCAN):
                pointer += 1
                if pointer < len(input_string):
                    symbol = input_string[pointer]
                    log += f"\nOne-Way: Scanned symbol '{symbol}'"
            
            # ----- PRINT OPERATIONS -----
            elif action.startswith(AbstractMachineUtils.PRINT):
                # Assume output is handled elsewhere; here we log the output.
                symbol = next(iter(self.transitions[state]))
                if output_string is None:
                    output_string = ""
                output_string += symbol
                log += f"\nState {state} Action: {action} -> Writing '{symbol}'"
            
            # ----- MEMORY OPERATIONS -----
            elif action.startswith(AbstractMachineUtils.READ):
                identifier = action.split("(")[1].rstrip(")")
                memory = data_memory[identifier]
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
                memory = data_memory[identifier]
                symbol = next(iter(self.transitions[state]))
                if isinstance(memory, Stack):
                    memory.push(symbol)
                elif isinstance(memory, Queue):
                    memory.enqueue(symbol)
                log += f"\nState {state} Action: {action} -> Writing '{symbol}' to {identifier}"
            
            # ----- Turing Machine Specific Operations -----
            elif action.startswith(AbstractMachineUtils.LEFT):
                identifier = action.split("(")[1].rstrip(")")
                memory = data_memory[identifier]
                symbol = memory.get_left()
                try:
                    replace = list(self.transitions[state][symbol])[0][0]
                except:
                    return symbol, pointer, input_string, data_memory, output_string
                if memory:
                    memory.move_left(replace)
                    log += f"\nState {state} Action: {action} -> Moving left on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move left on tape '{identifier}'"
            
            elif action.startswith(AbstractMachineUtils.RIGHT):
                identifier = action.split("(")[1].rstrip(")")
                memory = data_memory[identifier]
                symbol = memory.get_right()
                try:
                    replace = list(self.transitions[state][symbol])[0][0]
                except:
                    return symbol, pointer, input_string, data_memory, output_string
                if memory:
                    memory.move_right(replace)
                    log += f"\nState {state} Action: {action} -> Moving right on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move right on tape '{identifier}'"
            
            elif action.startswith(AbstractMachineUtils.UP):
                identifier = action.split("(")[1].rstrip(")")
                memory = data_memory[identifier]
                symbol = memory.get_up()
                try:
                    replace = list(self.transitions[state][symbol])[0][0]
                except:
                    return symbol, pointer, input_string, data_memory, output_string
                if memory:
                    memory.move_up(replace)
                    log += f"\nState {state} Action: {action} -> Moving up on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move up on tape '{identifier}'"
            
            elif action.startswith(AbstractMachineUtils.DOWN):
                identifier = action.split("(")[1].rstrip(")")
                memory = data_memory[identifier]
                symbol = memory.get_down()
                try:
                    replace = list(self.transitions[state][symbol])[0][0]
                except:
                    return symbol, pointer, input_string, data_memory, output_string
                if memory:
                    memory.move_down(replace)
                    log += f"\nState {state} Action: {action} -> Moving down on tape '{identifier}'"
                else:
                    log += f"\nState {state} Action: {action} -> Cannot move down on tape '{identifier}'"
        print(log)
        return symbol, pointer, input_string, data_memory, output_string