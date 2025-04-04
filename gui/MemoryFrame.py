import tkinter as tk
from model.AbstractMachineModel import Tape1D, Tape2D
from gui.TapeLabelFrame import TapeLabelFrame

class MemoryFrame(tk.Frame):
    def __init__(self, parent, memory_dict=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.memory_widgets = {}  # {identifier: (frame, label or TapeLabelFrame)}
        if memory_dict:
            self.create_widgets(memory_dict)

    def create_widgets(self, memory_dict):
        for identifier, content in memory_dict.items():
            self.add_memory_widget(identifier, content)

    def add_memory_widget(self, identifier, content):
        mem_frame = tk.Frame(self)
        
        if isinstance(content, (Tape1D, Tape2D)):
            mem_widget = TapeLabelFrame(mem_frame, identifier, content)
            mem_widget.pack(fill=tk.X)
        else:
            mem_widget = tk.Label(mem_frame, text=f"{identifier}: {content}", anchor="w")
            mem_widget.pack(fill=tk.X, padx=5, pady=2)
        
        mem_frame.pack(fill=tk.X, padx=5, pady=2)
        self.memory_widgets[identifier] = (mem_frame, mem_widget)

    def update_memory(self, new_memory_dict, identifier=None):
        if identifier:
            self.highlight_memory(identifier)
        
        for identifier, content in new_memory_dict.items():
            if identifier in self.memory_widgets:
                frame, widget = self.memory_widgets[identifier]
                if isinstance(content, (Tape1D, Tape2D)) and isinstance(widget, TapeLabelFrame):
                    widget.update_tape()
                elif isinstance(widget, tk.Label):
                    widget.config(text=f"{identifier}: {content}")
                else:
                    frame.destroy()
                    self.add_memory_widget(identifier, content)
            else:
                self.add_memory_widget(identifier, content)

    def highlight_memory(self, identifier, highlight_color="blue"):
        self.remove_highlight()
        if identifier in self.memory_widgets:
            frame, _ = self.memory_widgets[identifier]
            frame.config(highlightbackground=highlight_color,
                         highlightcolor=highlight_color,
                         highlightthickness=2)

    def remove_highlight(self):
        for identifier in self.memory_widgets:
            frame, _ = self.memory_widgets[identifier]
            frame.config(highlightthickness=0)

    def reset_memory(self, new_memory_dict):
        for frame, _ in self.memory_widgets.values():
            frame.destroy()
        self.memory_widgets.clear()
        self.create_widgets(new_memory_dict)