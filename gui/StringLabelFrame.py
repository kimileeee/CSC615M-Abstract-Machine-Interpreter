import tkinter as tk

class StringLabelFrame(tk.Frame):
    def __init__(self, parent, input_string="", **kwargs):
        super().__init__(parent, **kwargs)
        self.labels = []
        self.create_labels(input_string)

    def create_labels(self, input_string):
        # Clear existing labels
        for label in self.labels:
            label.destroy()
        self.labels = []
        
        # Create new labels
        for char in input_string:
            label = tk.Label(self, text=char, font=("Arial", 12), fg="black")
            label.pack(side=tk.LEFT, padx=2)
            self.labels.append(label)

        self.highlight_label(0)

    def update_string(self, new_string):
        self.create_labels(new_string)

    def highlight_label(self, index):
        for label in self.labels:
            label.config(fg="black")
        
        if 0 <= index < len(self.labels):
            self.labels[index].config(fg="red")
