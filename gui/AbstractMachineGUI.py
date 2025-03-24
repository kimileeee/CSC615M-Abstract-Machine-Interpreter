from model.AbstractMachineUtils import AbstractMachineUtils
from gui.StringLabelFrame import StringLabelFrame
from gui.MemoryFrame import MemoryFrame
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import math

class AbstractMachineGUI():
    WINDOW_TITLE = "FSM Visualization"
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 600
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600

    CIRCLE_COLOR = "lightblue"
    RADIUS = 25
    RADIUS_FINAL_SMALL = 21
    TRIANGLE_SIZE = 15
    STATE_LABEL_WIDTH = 15
    STATE_LABEL_HEIGHT = 20

    STATE_LABEL_FONT = ("Arial", 10, "bold")
    TRANSITION_LABEL_FONT = ("Arial", 10)
    STATE_NAME_FONT = ("Arial", 8, "bold")

    ARC_OFFSET_SELF_LOOP = 50
    ARC_OFFSET = 40
    LABEL_SPACING = 15 

    STEP_DELAY = 1000

    def __init__(self, machine):
        self.machine = machine
        self.node_items = {}  # state -> {"circle": id, "text": id, "pos": (x, y), ...}
        self.drag_data = {"state": None, "x": 0, "y": 0}
        
        self.root = ThemedTk(theme="breeze")
        self.root.title(self.WINDOW_TITLE)
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.root.resizable(0, 0)

        # Create a style for our output widget.
        self.style = ttk.Style(self.root)
        self.style.configure("Output.TEntry",
                        foreground="black",
                        fieldbackground="white",
                        background="white")
        
        self.style.map("Output.TEntry",
                foreground=[('disabled', 'black')],
                fieldbackground=[('disabled', 'white')])
        
        self.style.configure("Command.TEntry",
                        foreground="black",
                        fieldbackground="white",
                        background="white")
        
        self.style.map("Command.TEntry",
                foreground=[('disabled', 'black')],
                fieldbackground=[('disabled', 'white')])

        # Canvas for state diagram
        self.canvas = tk.Canvas(self.root, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.Y)

        # Frame for menu
        self.menu_frame = ttk.Frame(self.root, width=self.WINDOW_WIDTH - self.CANVAS_WIDTH, height=self.WINDOW_HEIGHT)
        self.menu_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)
        
        ttk.Label(self.menu_frame, text="Menu").pack(pady=5)

        # Input
        ttk.Label(self.menu_frame, text="Input:").pack()
        self.input_entry = ttk.Entry(self.menu_frame, justify="center")
        self.input_entry.pack()

        self.set_input_button = ttk.Button(self.menu_frame, text="Set Input", command=self.initialize)
        self.set_input_button.pack(pady=5)

        # Output
        ttk.Label(self.menu_frame, text="Output:").pack()
        self.output = tk.StringVar()
        self.output_entry = ttk.Entry(self.menu_frame, textvariable=self.output, state="disabled", justify="center", style="Output.TEntry")
        self.output_entry.pack(pady=5)

        # Buttons for stepping
        self.steps_btn_frame = ttk.Frame(self.menu_frame)
        self.steps_btn_frame.pack(pady=10)

        self.prev_button = ttk.Button(self.steps_btn_frame, text="<", command=self.prev_step, state=tk.DISABLED)
        self.prev_button.grid(row=0, column=0)
        self.next_button = ttk.Button(self.steps_btn_frame, text=">", command=self.next_step, state=tk.DISABLED)
        self.next_button.grid(row=0, column=1)

        # Buttons for full run
        self.run_button = ttk.Button(self.steps_btn_frame, text="Run", command=self.start_run, state=tk.DISABLED)
        self.run_button.grid(row=0, column=2)
        self.reset_button = ttk.Button(self.menu_frame, text="Reset", command=self.stop_run, state=tk.DISABLED)
        self.reset_button.pack(pady=5)

        separator = ttk.Separator(self.menu_frame, orient="horizontal")
        separator.pack(fill="x", pady=5)

        # Command
        ttk.Label(self.menu_frame, text="Command:").pack()
        self.command = tk.StringVar()
        self.command_label = ttk.Entry(self.menu_frame, textvariable=self.command, justify="center", state="disabled", style="Command.TEntry")
        self.command_label.pack(pady=5)

        # Input trace
        if self.machine.input_tape == None:
            ttk.Label(self.menu_frame, text="Input Trace:").pack()
            self.input_string_frame = StringLabelFrame(self.menu_frame, input_string = "")
            self.input_string_frame.pack(pady=5, padx=5)
        else:
            self.input_string_frame = None

        # Memory trace
        ttk.Label(self.menu_frame, text="Memory:").pack()
        self.memory_frame = MemoryFrame(self.menu_frame, self.machine.data_memory)
        self.memory_frame.pack(fill=tk.BOTH, pady=5, padx=5)

        self.draw_state_diagram()
        self.update_state_indicator()
        self.update_input_display()

    def initialize(self):
        # Initialize machine simulation (backend) with the input.
        self.machine.initialize(self.input_entry.get().strip("\n"))
        
        self.command.set(self.machine.states[self.machine.current_state])
        if self.input_string_frame:
            self.input_string_frame.update_string(self.machine.input_string)
        self.update_state_indicator()
        self.update_input_display()
        self.update_memory()

        # Enable buttons after input is set.
        self.set_input_button.config(state=tk.DISABLED)
        self.prev_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.run_button.config(state=tk.NORMAL)
        
    def start_run(self):
        self.running = True

        # Disable input entry and buttons while running.
        self.input_entry.config(state=tk.DISABLED)
        self.prev_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        self.run_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)
        
        # Delay the first auto-step so that the starting state is visible.
        self.root.after(self.STEP_DELAY, self.auto_step)

    def stop_run(self):
        self.running = False

        # Reset the machine to its initial state.
        self.machine.reset()
        self.reset_gui()

    def reset_gui(self):
        self.machine.initialize("")  

        # Clear the input entry widget and re-enable it.
        self.input_entry.config(state=tk.NORMAL)
        self.input_entry.delete(0, tk.END)
        
        self.command.set("")
        if self.input_string_frame:
            self.input_string_frame.update_string("")
        
        # Reset button states.
        self.set_input_button.config(state=tk.NORMAL)
        self.prev_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        self.run_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        
        # Reset the state diagram highlighting.
        self.update_output("")
        self.update_state_indicator()
        self.update_input_display()
        self.memory_frame.update_memory(self.machine.data_memory)

    def auto_step(self):
        if self.running and self.machine.current_state != AbstractMachineUtils.ACCEPT and self.machine.current_state != AbstractMachineUtils.REJECT:
            self.next_step()
            if self.running:
                self.root.after(self.STEP_DELAY, self.auto_step)

    def next_step(self):
        result = self.machine.next_step()
        
        try:
            self.command.set(self.machine.states[self.machine.current_state])
        except KeyError:
            self.command.set("")
        
        self.update_output(result)
        self.update_state_indicator()
        self.update_input_display()
        self.update_memory()

        if self.machine.current_state == AbstractMachineUtils.ACCEPT:
            self.next_button.config(state=tk.DISABLED)
            self.prev_button.config(state=tk.NORMAL)

    def prev_step(self):
        result = self.machine.prev_step()
        
        self.command.set(self.machine.states[self.machine.current_state])
        self.update_output(result)
        self.update_state_indicator()
        self.update_input_display()
        self.update_memory()

        if not self.machine.history:
            self.prev_button.config(state=tk.DISABLED)

        if self.machine.current_state != AbstractMachineUtils.ACCEPT:
            self.next_button.config(state=tk.NORMAL)
    
    def update_input_display(self):
        if self.machine.pointer < len(self.machine.input_string):
            if self.input_string_frame:
                self.input_string_frame.highlight_label(self.machine.pointer)

    def update_output(self, text):
        self.output.set(text)
        # Update the field background based on the text.
        if text == "ACCEPTED":
            self.style.configure("Output.TEntry", fieldbackground="#b4d3b2", background="#b4d3b2")
        elif text == "REJECTED":
            self.style.configure("Output.TEntry", fieldbackground="#d3b2b4", background="#d3b2b4")
        else:
            self.style.configure("Output.TEntry", fieldbackground="white", background="white")
        # Even though the widget is disabled, the style map ensures the text stays black.

    def update_memory(self):
        identifier = ""
        if "(" in self.command.get():
            identifier = self.command.get().split("(")[1].split(")")[0]
            self.memory_frame.update_memory(self.machine.data_memory, identifier)
        else:
            self.memory_frame.update_memory(self.machine.data_memory)
            self.memory_frame.remove_highlight()
        
    def run(self):
        self.root.mainloop()

    def draw_state_diagram(self):
        center_x = self.CANVAS_WIDTH // 2
        center_y = self.CANVAS_HEIGHT // 2
        layout_radius = min(self.CANVAS_WIDTH, self.CANVAS_HEIGHT) // 2 - 50

        self.states = list(self.machine.states.keys())
        for i, state in enumerate(self.states):
            angle = 2 * math.pi * i / len(self.states)
            x = center_x + layout_radius * math.cos(angle)
            y = center_y + layout_radius * math.sin(angle)

            if state == self.machine.start_state:
                self.draw_state(state, (x, y), "start")
            elif state == AbstractMachineUtils.ACCEPT:
                self.draw_state(state, (x, y), "accept")
            else:
                self.draw_state(state, (x, y))

        self.redraw_transitions()

    def draw_state(self, state, pos, type="normal"):
        x, y = pos
        extra_items = {}
        
        circle = self.canvas.create_oval(x - self.RADIUS, y - self.RADIUS, x + self.RADIUS, y + self.RADIUS,
                                              fill=self.CIRCLE_COLOR, outline="black", width=2, tags=("node", state))
        
        if type == "start":
            points = [
                x - self.RADIUS, y,
                x - self.RADIUS - self.TRIANGLE_SIZE, y - self.RADIUS/2,
                x - self.RADIUS - self.TRIANGLE_SIZE, y + self.RADIUS/2
            ]
            triangle = self.canvas.create_polygon(points, fill="black", outline="black", tags=("node", state))
            extra_items["triangle"] = triangle

        elif type == "accept":
            inner_circle = self.canvas.create_oval(x - self.RADIUS_FINAL_SMALL, y - self.RADIUS_FINAL_SMALL,
                                                     x + self.RADIUS_FINAL_SMALL, y + self.RADIUS_FINAL_SMALL,
                                                     fill=self.CIRCLE_COLOR, outline="black", width=2, tags=("node", state))
            extra_items["inner_circle"] = inner_circle
            
        state_label = state
        command  = self.machine.states[state]
        mem = ""
        if command:
            if "(" in command:
                command, mem = command.split("(")
                command = command.strip()
                mem = mem.strip(")")
            state_label = AbstractMachineUtils.shorthand_actions.get(command)
            if mem != "":
                state_label += f"({mem})"
        
        text = self.canvas.create_text(x, y, text=state_label, font=self.STATE_LABEL_FONT, tags=("node", state))
        
        label_rect = None
        label_text = None
        label_x = x + self.RADIUS - self.STATE_LABEL_WIDTH / 2
        label_y = y + self.RADIUS - self.STATE_LABEL_HEIGHT / 4

        if state not in [AbstractMachineUtils.ACCEPT, AbstractMachineUtils.REJECT]:
            label_rect = self.canvas.create_rectangle(
                label_x - self.STATE_LABEL_WIDTH / 2, label_y - self.STATE_LABEL_HEIGHT / 2,
                label_x + self.STATE_LABEL_WIDTH / 2, label_y + self.STATE_LABEL_HEIGHT / 2,
                fill=self.CIRCLE_COLOR, outline="black", width=2, tags=("node", state)
            )
            label_text = self.canvas.create_text(label_x, label_y, text=state, 
                                                font=self.STATE_NAME_FONT, tags=("node", state))
            extra_items["label_rect"] = label_rect
            extra_items["label_text"] = label_text

        # Store all items (circle, text, and any extras) along with position.
        self.node_items[state] = {"circle": circle, "text": text, "pos": (x, y)}
        self.node_items[state].update(extra_items)
        
        for item in (circle, text) + tuple(extra_items.values()):
            self.canvas.tag_bind(item, "<ButtonPress-1>", self.on_node_press)
            self.canvas.tag_bind(item, "<B1-Motion>", self.on_node_motion)
            self.canvas.tag_bind(item, "<ButtonRelease-1>", self.on_node_release)

    def draw_arrow_with_labels(self, src, dst, symbols, replace_dst=None):
        """Draws an arrow from src to dst and stacks all labels (symbols) above the arrow."""
        x1, y1 = self.node_items[src]["pos"]
        x2, y2 = self.node_items[dst]["pos"]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)

        # Handle self-loop differently.
        if src == dst or dist == 0:
            # Instead of an arc, create a smoothed polyline for a self-loop.
            # We'll choose two boundary points on the circle and control points above.
            loop_offset = 30  # How far upward the loop should go.
            horizontal_offset = self.RADIUS / 2  # How far left/right from center.
            # Compute start and end points on the circle boundary (top-left and top-right)
            start_x = x1 - horizontal_offset
            start_y = y1 - self.RADIUS
            end_x = x1 + horizontal_offset
            end_y = y1 - self.RADIUS
            # Compute control points that push the curve upward.
            control1_x = start_x
            control1_y = start_y - loop_offset
            control2_x = end_x
            control2_y = end_y - loop_offset

            self.canvas.create_line(start_x, start_y,
                                    control1_x, control1_y,
                                    control2_x, control2_y,
                                    end_x, end_y,
                                    smooth=True, arrow=tk.LAST, width=2, tags="transition")
            # Place label(s) near the top of the loop.
            base_label_x = x1
            base_label_y = control1_y - 10
            for i, sym in enumerate(symbols):
                symbol = sym.split("/")[0]
                replace = sym.split("/")[1] if "/" in sym else None
                if replace == None:
                    label_text = f"{symbol}"
                elif replace != None and symbol == replace:
                    label_text = f"{symbol}"
                else:
                    label_text = f"{symbol} / {replace}"

                self.canvas.create_text(base_label_x, base_label_y - i * self.LABEL_SPACING,
                                        text=label_text, fill="black", font=self.TRANSITION_LABEL_FONT, tags="transition")
            return

        # Compute the start and end points along the boundary of the circles.
        offset_x = (dx / dist) * self.RADIUS
        offset_y = (dy / dist) * self.RADIUS
        start_x = x1 + offset_x
        start_y = y1 + offset_y
        end_x = x2 - offset_x
        end_y = y2 - offset_y

        # Check if a reverse transition exists (an arrow from dst to src).
        reverse_exists = any(src in dests for dests in self.machine.transitions.get(dst, {}).values())

        # Compute midpoint and perpendicular unit vector for arc control point.
        mid_x = (start_x + end_x) / 2
        mid_y = (start_y + end_y) / 2
        perp_dx = -dy / dist
        perp_dy = dx / dist

        if reverse_exists:
            offset_amount = self.ARC_OFFSET
            ctrl_x = mid_x + perp_dx * offset_amount
            ctrl_y = mid_y + perp_dy * offset_amount
            self.canvas.create_line(start_x, start_y, ctrl_x, ctrl_y, end_x, end_y,
                                    smooth=True, arrow=tk.LAST, width=2, tags="transition")
            base_label_x, base_label_y = ctrl_x, ctrl_y
        else:
            self.canvas.create_line(start_x, start_y, end_x, end_y,
                                    arrow=tk.LAST, width=2, tags="transition")
            base_label_x = mid_x + perp_dx * 15
            base_label_y = mid_y + perp_dy * 15

        for i, sym in enumerate(symbols):
            symbol = sym.split("/")[0]
            replace = sym.split("/")[1] if "/" in sym else None
            if replace == None:
                label_text = f"{symbol}"
            elif replace != None and symbol == replace:
                label_text = f"{symbol}"
            else:
                label_text = f"{symbol} / {replace}"
            
            self.canvas.create_text(base_label_x, base_label_y - i * self.LABEL_SPACING,
                                    text=label_text, fill="black", font=self.TRANSITION_LABEL_FONT, tags="transition")

    def redraw_transitions(self):
        self.canvas.delete("transition")
        arrow_data = {}
        for src, trans in self.machine.transitions.items():
            for symbol, dest_set in trans.items():
                for dst in dest_set:
                    # If destination is a tuple, consider only its second element.
                    if isinstance(dst, tuple):
                        arrow_data.setdefault((src, dst[1]), []).append(f"{symbol}/{dst[0]}")
                    else:
                        arrow_data.setdefault((src, dst), []).append(symbol)
                    
        for (src, dst), symbols in arrow_data.items():
            self.draw_arrow_with_labels(src, dst, symbols)


    def update_state_indicator(self):
        for state, items in self.node_items.items():
            self.canvas.itemconfig(items["circle"], outline="black", width=2)
        current = self.machine.current_state
        if current in self.node_items:
            self.canvas.itemconfig(self.node_items[current]["circle"], outline="red", width=4)

    def on_node_press(self, event):
        item = self.canvas.find_closest(event.x, event.y)[0]
        tags = self.canvas.gettags(item)
        state = None
        for tag in tags:
            if tag in self.node_items:
                state = tag
                break
        if state is None:
            return
        self.drag_data["state"] = state
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_node_motion(self, event):
        state = self.drag_data["state"]
        if state is None:
            return
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

        # Move primary items.
        self.canvas.move(self.node_items[state]["circle"], dx, dy)
        self.canvas.move(self.node_items[state]["text"], dx, dy)
        # Move extra items if they exist.
        if "triangle" in self.node_items[state]:
            self.canvas.move(self.node_items[state]["triangle"], dx, dy)
        if "inner_circle" in self.node_items[state]:
            self.canvas.move(self.node_items[state]["inner_circle"], dx, dy)
        # Move the square label items.
        if "label_rect" in self.node_items[state]:
            self.canvas.move(self.node_items[state]["label_rect"], dx, dy)
        if "label_text" in self.node_items[state]:
            self.canvas.move(self.node_items[state]["label_text"], dx, dy)

        x, y = self.node_items[state]["pos"]
        self.node_items[state]["pos"] = (x + dx, y + dy)
        self.redraw_transitions()

    def on_node_release(self, event):
        self.drag_data["state"] = None