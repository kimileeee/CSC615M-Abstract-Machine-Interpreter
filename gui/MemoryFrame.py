import tkinter as tk

class MemoryFrame(tk.Frame):
    def __init__(self, parent, memory_dict=None, **kwargs):
        """
        :param parent: The parent widget.
        :param memory_dict: An optional dictionary mapping memory identifiers
                            to their initial contents.
        :param kwargs: Additional keyword arguments for the Frame.
        """
        super().__init__(parent, **kwargs)
        
        self.memory_widgets = {}  # {identifier: (frame, label)}
        
        # If an initial memory dictionary is provided, create widgets for each.
        if memory_dict:
            self.create_widgets(memory_dict)

    def create_widgets(self, memory_dict):
        for identifier, content in memory_dict.items():
            self.add_memory_widget(identifier, content)

    def add_memory_widget(self, identifier, content):
        mem_frame = tk.Frame(self, relief="groove")
        mem_label = tk.Label(mem_frame, text=f"{identifier}: {content}", anchor="w")
        mem_label.pack(fill=tk.X, padx=5, pady=2)
        mem_frame.pack(fill=tk.X, padx=5, pady=2)
        self.memory_widgets[identifier] = (mem_frame, mem_label)

    def update_memory(self, new_memory_dict, identifier=None):
        if identifier:
            self.highlight_memory(identifier)
        
        for identifier, content in new_memory_dict.items():
            if identifier in self.memory_widgets:
                frame, label = self.memory_widgets[identifier]
                label.config(text=f"{identifier}: {content}")
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

