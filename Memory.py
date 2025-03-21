from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop() if self.stack else None  # Return None if empty
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __repr__(self):
        return repr(self.stack)

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.popleft() if self.queue else None  # Return None if empty
    
    def peek(self):
        return self.queue[0] if self.queue else None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __repr__(self):
        return repr(list(self.queue))

class Tape1D:
    def __init__(self, blank_symbol='#'):
        self.tape = {}  # Sparse representation
        self.head = 0
        self.blank = blank_symbol

    def input_tape(self, input_string):
        for i, symbol in enumerate(input_string):
            self.tape[i] = symbol
    
    def read(self):
        return self.tape.get(self.head, self.blank)
    
    def write(self, symbol):
        if symbol == self.blank and self.head in self.tape:
            del self.tape[self.head]  # Remove empty cells
        else:
            self.tape[self.head] = symbol
    
    def move_left(self):
        self.head -= 1
    
    def move_right(self):
        self.head += 1
    
    def __repr__(self):
        min_index = min(self.tape.keys(), default=0)
        max_index = max(self.tape.keys(), default=0)
        return ''.join(self.tape.get(i, self.blank) for i in range(min_index, max_index + 1))

class Tape2D:
    def __init__(self, blank_symbol='#'):
        self.tape = {}  # Sparse representation
        self.head_x = 0
        self.head_y = 0
        self.blank = blank_symbol
    
    def read(self):
        return self.tape.get((self.head_x, self.head_y), self.blank)
    
    def write(self, symbol):
        if symbol == self.blank and (self.head_x, self.head_y) in self.tape:
            del self.tape[(self.head_x, self.head_y)]  # Remove empty cells
        else:
            self.tape[(self.head_x, self.head_y)] = symbol
    
    def move_left(self):
        self.head_x -= 1
    
    def move_right(self):
        self.head_x += 1
    
    def move_up(self):
        self.head_y -= 1
    
    def move_down(self):
        self.head_y += 1
    
    def __repr__(self):
        min_x = min((x for x, _ in self.tape.keys()), default=0)
        max_x = max((x for x, _ in self.tape.keys()), default=0)
        min_y = min((y for _, y in self.tape.keys()), default=0)
        max_y = max((y for _, y in self.tape.keys()), default=0)
        
        result = []
        for y in range(min_y, max_y + 1):
            row = ''.join(self.tape.get((x, y), self.blank) for x in range(min_x, max_x + 1))
            result.append(row)
        return '\n'.join(result)
