import tkinter as tk
from model.AbstractMachineModel import Tape1D, Tape2D

class TapeLabelFrame(tk.Frame):
    def __init__(self, parent, identifier, tape, **kwargs):
        super().__init__(parent, **kwargs)
        self.tape = tape
        self.tape_label = tk.Label(self, text=identifier+": ", font=("Arial", 12))
        self.tape_label.pack(side=tk.LEFT)
        self.tape_content_frame = tk.Frame(self)
        self.labels = {}
        self.create_labels()
        self.tape_content_frame.pack()

    def create_labels(self):
        for label in self.labels.values():
            label.destroy()
        self.labels = {}
        
        if isinstance(self.tape, Tape1D):
            min_index = min(self.tape.tape.keys(), default=0)
            max_index = max(self.tape.tape.keys(), default=0)
            for i in range(min_index, max_index + 1):
                char = self.tape.tape.get(i, self.tape.blank)
                label = tk.Label(self.tape_content_frame, text=char, font=("Arial", 12), fg="black")
                label.pack(side=tk.LEFT, padx=2)
                self.labels[i] = label

            self.highlight_label(self.tape.head)

        elif isinstance(self.tape, Tape2D):
            # for widget in self.tape_content_frame.winfo_children():
            #     widget.destroy()

            min_x = min((x for x, _ in self.tape.tape.keys()), default=0)
            max_x = max((x for x, _ in self.tape.tape.keys()), default=0)
            min_y = min((y for _, y in self.tape.tape.keys()), default=0)
            max_y = max((y for _, y in self.tape.tape.keys()), default=0)

            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    char = self.tape.tape.get((x, y), self.tape.blank)
                    label = tk.Label(self.tape_content_frame, text=char, font=("Arial", 12), fg="black")
                    label.grid(row=y, column=x, padx=2, pady=2)
                    self.labels[(x, y)] = label

            self.highlight_label((self.tape.head_x, self.tape.head_y))

    def update_tape(self):
        self.create_labels()

    def highlight_label(self, index):
        for label in self.labels.values():
            label.config(fg="black")
        
        if isinstance(self.tape, Tape1D):
            if index in self.labels:
                self.labels[index].config(fg="red")
        elif isinstance(self.tape, Tape2D):
            if index in self.labels:
                self.labels[index].config(fg="red")