import tkinter as tk
from model.AbstractMachineModel import Tape1D, Tape2D

class TapeLabelFrame(tk.Frame):
    def __init__(self, parent, identifier, tape, **kwargs):
        super().__init__(parent, **kwargs)
        self.tape = tape
        self.tape_label = tk.Label(self, text=identifier+": ", font=("Arial", 12))
        self.tape_label.pack(side=tk.LEFT)
        self.tape_content_frame = tk.Frame(self)
        self.labels = []
        self.create_labels()
        self.tape_content_frame.pack()

    def create_labels(self):
        for label in self.labels:
            label.destroy()
        self.labels = []
        
        min_index = min(self.tape.tape.keys(), default=0)
        max_index = max(self.tape.tape.keys(), default=0)
        for i in range(min_index, max_index + 1):
            char = self.tape.tape.get(i, self.tape.blank)
            label = tk.Label(self.tape_content_frame, text=char, font=("Arial", 12), fg="black")
            label.pack(side=tk.LEFT, padx=2)
            self.labels.append(label)

        self.highlight_label(self.tape.head)

    def update_tape(self):
        self.create_labels()

    def highlight_label(self, index):
        for label in self.labels:
            label.config(fg="black")
        
        offset = min(self.tape.tape.keys(), default=0)
        if offset <= index < offset + len(self.labels):
            self.labels[index - offset].config(fg="red")