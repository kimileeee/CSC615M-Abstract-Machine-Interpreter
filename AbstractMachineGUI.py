from AbstractMachineUtils import AbstractMachineUtils
import tkinter as tk
import math

class AbstractMachineGUI():

    WINDOW_TITLE = "FSM Visualization"
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600
    RADIUS = 20
    ARC_OFFSET_SELF_LOOP = 50
    ARC_OFFSET = 40
    LABEL_SPACING = 15 
    STEP_DELAY = 1000

    def __init__(self, machine):
        self.machine = machine
        self.node_items = {}  # state -> {"circle": id, "text": id, "pos": (x, y)}
        self.drag_data = {"state": None, "x": 0, "y": 0}

        self.root = tk.Tk()
        self.root.title(self.WINDOW_TITLE)

        # Canvas for state diagram
        self.canvas = tk.Canvas(self.root, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.Y)

        # Frame for menu
        self.menu_frame = tk.Frame(self.root, width=self.WINDOW_WIDTH - self.CANVAS_WIDTH, height=self.WINDOW_HEIGHT)
        self.menu_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        tk.Label(self.menu_frame, text="Menu").pack(pady=5)

        # Input and output
        tk.Label(self.menu_frame, text="Input:").pack()
        self.input_entry = tk.Entry(self.menu_frame)
        self.input_entry.pack()

        tk.Label(self.menu_frame, text="Output:").pack()
        self.output = tk.StringVar()
        self.output_label = tk.Label(self.menu_frame, textvariable=self.output)
        self.output_label.pack(pady=5)

        # Display input with pointer indicator.
        tk.Label(self.menu_frame, text="Input Trace:").pack()
        self.tape_label = tk.Label(self.menu_frame, text="", font=("Arial", 12))
        self.tape_label.pack(pady=5)

        # Buttons for stepping
        self.steps_btn_frame = tk.Frame(self.menu_frame)
        self.steps_btn_frame.pack(pady=10)

        prev_button = tk.Button(self.steps_btn_frame, text="Prev", command=self.prev_step)
        prev_button.pack(side=tk.LEFT, padx=5)
        next_button = tk.Button(self.steps_btn_frame, text="Next", command=self.next_step)
        next_button.pack(side=tk.RIGHT, padx=5)

        # Buttons for full run
        run_button = tk.Button(self.menu_frame, text="Run", command=self.start_run)
        run_button.pack(pady=5)
        stop_button = tk.Button(self.menu_frame, text="Stop", command=self.stop_run)
        stop_button.pack(pady=5)

        self.draw_state_diagram()
        self.update_state_indicator()
        self.update_input_display()

    def start_run(self):
        # Initialize machine simulation (backend) with the input.
        self.machine.initialize(self.input_entry.get().strip("\n"))
        self.update_state_indicator()
        self.update_input_display()
        self.running = True
        # Delay the first auto-step so that the starting state A is shown for a moment.
        self.root.after(self.STEP_DELAY, self.auto_step)

    def stop_run(self):
        self.running = False

    def auto_step(self):
        if self.running and self.machine.current_state != AbstractMachineUtils.ACCEPT:
            self.next_step()
            if self.running:
                self.root.after(self.STEP_DELAY, self.auto_step)

    def next_step(self):
        result = self.machine.next_step()
        self.output.set(result)
        self.update_state_indicator()
        self.update_input_display()

    def prev_step(self):
        result = self.machine.prev_step()
        self.output.set(result)
        self.update_state_indicator()
        self.update_input_display()
    
    def update_input_display(self):
        """
        Update the tape display with the pointer highlighted.
        For simplicity, the pointer letter is wrapped in square brackets.
        """
        tape = self.machine.input_string
        pointer = self.machine.pointer
        if pointer < len(tape):
            highlighted = tape[:pointer] + "[" + tape[pointer] + "]" + tape[pointer+1:]
        else:
            # When pointer is at the end, indicate position with empty brackets.
            highlighted = tape + " []"
        self.tape_label.config(text=highlighted)

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
        color = "lightblue"
        if type == "start":
            color = "lightyellow"
        elif type == "accept":
            color = "lightgreen"
        circle = self.canvas.create_oval(x - self.RADIUS, y - self.RADIUS, x + self.RADIUS, y + self.RADIUS,
                                         fill=color, outline="black", width=2, tags=("node", state))
        text = self.canvas.create_text(x, y, text=state, font=("Arial", 12, "bold"), tags=("node", state))
        self.node_items[state] = {"circle": circle, "text": text, "pos": (x, y)}
        for item in (circle, text):
            self.canvas.tag_bind(item, "<ButtonPress-1>", self.on_node_press)
            self.canvas.tag_bind(item, "<B1-Motion>", self.on_node_motion)
            self.canvas.tag_bind(item, "<ButtonRelease-1>", self.on_node_release)

    def draw_arrow_with_labels(self, src, dst, symbols):
        """Draws an arrow from src to dst and stacks all labels (symbols) above the arrow."""
        x1, y1 = self.node_items[src]["pos"]
        x2, y2 = self.node_items[dst]["pos"]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)

        # Handle self-loop.
        if src == dst or dist == 0:
            loop_radius = self.RADIUS + 10
            self.canvas.create_arc(x1 - loop_radius, y1 - loop_radius,
                                   x1 + loop_radius, y1 + loop_radius,
                                   start=0, extent=300, style=tk.ARC, outline="black", tags="transition")
            base_label_y = y1 - loop_radius - 10
            # Draw each label with vertical spacing.
            for i, sym in enumerate(symbols):
                self.canvas.create_text(x1, base_label_y - i * self.LABEL_SPACING, text=sym,
                                        fill="black", font=("Arial", 10), tags="transition")
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
            # Use ARC_OFFSET for bidirectional curves.
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

        # Draw all symbols.
        for i, sym in enumerate(symbols):
            self.canvas.create_text(base_label_x, base_label_y - i * self.LABEL_SPACING,
                                    text=sym, fill="black", font=("Arial", 10), tags="transition")

    def redraw_transitions(self):
        self.canvas.delete("transition")
        # Group transitions by (src, dst)
        arrow_data = {}
        for src, trans in self.machine.transitions.items():
            for symbol, dest_set in trans.items():
                for dst in dest_set:
                    arrow_data.setdefault((src, dst), []).append(symbol)

        # Draw one arrow per (src, dst) pair with all the symbols as labels.
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
        self.canvas.move(self.node_items[state]["circle"], dx, dy)
        self.canvas.move(self.node_items[state]["text"], dx, dy)
        x, y = self.node_items[state]["pos"]
        self.node_items[state]["pos"] = (x + dx, y + dy)
        self.redraw_transitions()

    def on_node_release(self, event):
        self.drag_data["state"] = None
