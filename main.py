import tkinter as tk
from tkinter import ttk, scrolledtext
from ttkthemes import ThemedTk
from antlr4 import *
from automata.AbstractMachineLexer import AbstractMachineLexer
from automata.AbstractMachineParser import AbstractMachineParser
from AbstractMachineInterpreter import AbstractMachineInterpreter
from gui.AbstractMachineFrame import AbstractMachineFrame

def check_lexer(tokens):
    lexer_bool = True
    for token in tokens:
        if token.channel == AbstractMachineLexer.ERRORS:
            print(f"Line {token.line}, Column {token.column}: Invalid token '{token.text}'")
            lexer_bool = False
    return lexer_bool

def process_code(code_input, compile_output, compile_button, parent_gui):
    source_code = code_input.get("1.0", tk.END)
    
    input_stream = InputStream(source_code)
    lexer = AbstractMachineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    if check_lexer(token_stream.tokens):
        parser = AbstractMachineParser(token_stream)
        try:
            tree = parser.program()

            if parser.getNumberOfSyntaxErrors() > 0:
                compile_output.set("Syntax errors detected.\n")
                raise Exception("Syntax errors detected.")
            
            interpreter = AbstractMachineInterpreter()
            interpreter.visit(tree)

            for widget in parent_gui.winfo_children():
                widget.destroy()
            
            machine_gui = AbstractMachineFrame(interpreter.machine, parent=parent_gui)

            code_input.config(state=tk.DISABLED)
            compile_button.config(state=tk.DISABLED)
            compile_output.set("Compilation successful.\n")
        except Exception as e:
            compile_output.set(f"Errors found. Please check your source code.\n")
    else:
        compile_output.set("Errors found. Please check your source code.\n")

def edit_code(code_input, compile_output, compile_button, parent_gui):
    code_input.config(state=tk.NORMAL)

    compile_output.set("")
    compile_button.config(state=tk.NORMAL)

    for widget in parent_gui.winfo_children():
        widget.destroy()

def create_gui():
    root = ThemedTk(theme=TK_THEME)
    root.title(WINDOW_TITLE)
    root.resizable(False, False)

    style = ttk.Style(root)
    style.configure("Compile.TEntry",
                             foreground="black",
                             fieldbackground="white",
                             background="white")
    style.map("Compile.TEntry",
                    foreground=[('disabled', 'black')],
                    fieldbackground=[('disabled', 'white')])

    code_frame = ttk.Frame(root)
    code_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)
    
    # Code input
    input_label = ttk.Label(code_frame, text="Enter Code:")
    input_label.pack()
    
    code_input = scrolledtext.ScrolledText(code_frame, width=40, bg="white", wrap=tk.WORD)
    code_input.pack()
    
    # Compile message
    compile_label = ttk.Label(code_frame, text="Compile Messages:")
    compile_label.pack()
    
    compile_output = tk.StringVar()
    compile_message = ttk.Entry(code_frame, width=40, state=tk.DISABLED, 
                                textvariable=compile_output, style="Compile.TEntry")
    compile_message.pack()

    # Buttons
    buttons_frame = ttk.Frame(code_frame)
    buttons_frame.pack(pady=5)

    # Compile button
    compile_button = ttk.Button(buttons_frame, text="Compile", 
                           command=lambda: process_code(code_input, compile_output, compile_button, machine_container))
    compile_button.pack(side=tk.LEFT, pady=5, padx=5)

    # Clear button
    clear_button = ttk.Button(buttons_frame, text="Edit", 
                           command=lambda: edit_code(code_input, compile_output, compile_button, machine_container))
    clear_button.pack(side=tk.RIGHT, pady=5)

    # machine visualization frame.
    machine_container = ttk.Frame(root)
    machine_container.pack(side=tk.RIGHT, expand=True, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    WINDOW_TITLE = "Abstract Machine Interpreter"
    TK_THEME = "breeze"
    create_gui()
