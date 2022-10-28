import turtle
import string
from tkinter import StringVar, ttk
import tkinter as tk
from ttkwidgets import TickScale

class App:
    def __init__(self, master):
        
        """Initialize class App
        params
        ============
        master: window
        """
        self.master = master
        self.master.title("Raw Turtle")
        
        self.clicked = StringVar()
        self.clicked.set("Custom")
        
        self.create_widgets()
        self.create_turtle_screen()
        self.master.title("Turtletrees")

    def create_widgets(self):
        
        """
        Function creating and arranging widgets in left panel
        """
        
        self.frameA = tk.Frame()
        self.frameA.pack(fill=tk.BOTH, side=tk.LEFT, padx=15)
        self.frameA.columnconfigure([0, 1], minsize=40)
        self.frameA.rowconfigure(list(range(1, 16)), minsize=20)

        # Description
        self.description = ttk.Label(master=self.frameA, # $$
                                     text="Welcome to the Turtle Trees Simulator!",
                                     font=("Arial", 13),
                                     justify=tk.CENTER)
        self.description.grid(row=0, column=0,
                              columnspan=2, rowspan=2,
                              sticky="w")

        # Preset values
        options = ["Tree", "Custom"]
        self.axiom_label = ttk.Label(master=self.frameA, text="Select an organic structure:", font=("Arial", 12))
        self.axiom_label.grid(row=5, column=1, columnspan=2, sticky="nesw")
        self.preselects = tk.OptionMenu(self.frameA, self.clicked, *options, command=self.preset_autofill)
        # TODO: use ttk.OptionMenu instead, but this makes first dropdown option disappear
        self.preselects.grid(row=6, column=1, columnspan=2, sticky="nesw", pady=10)

        # angle input
        self.lbl_angle = ttk.Label(master=self.frameA, text="Angle: ")
        self.ent_angle = ttk.Entry(master=self.frameA)
        self.ent_angle.insert(0, '20')
        self.lbl_angle.grid(row=7, column=0, sticky="e", pady=5)
        self.ent_angle.grid(row=7, column=1, sticky="nesw", pady=5)

        # length input
        self.lbl_length = ttk.Label(master=self.frameA, text="Length: ")
        self.ent_length = ttk.Entry(master=self.frameA)
        self.ent_length.insert(0, '15')
        self.lbl_length.grid(row=8, column=0, sticky="e", pady=5)
        self.ent_length.grid(row=8, column=1, sticky="nesw", pady=5)

        # iteractions slider
        self.scl_iters = TickScale(master=self.frameA, orient='horizontal',
                                   from_=1, to=5, resolution=1,
                                   showvalue=True, length=20)
        self.lbl_iters = ttk.Label(master=self.frameA, text="Iterations: ")
        self.lbl_iters.grid(row=9, column=0, sticky="e", pady=5)
        self.scl_iters.grid(row=9, column=1, sticky="nesw", pady=5)
        self.scl_iters.set(2) ##$$

        # reproduction rules
        self.rep_label = ttk.Label(master=self.frameA, text="Reproduction Rules:", font=("Arial", 12))
        self.rep_label.grid(row=10, column=1, columnspan=2, sticky="nesw", pady=10)

        self.lbl_ruleA = ttk.Label(master=self.frameA, text="A → ")
        self.ent_ruleA = ttk.Entry(master=self.frameA)
        self.ent_ruleA.insert(0, 'B+[[A]-A]-B[-BA]+A')
        self.lbl_ruleA.grid(row=11, column=0, sticky="e", pady=5)
        self.ent_ruleA.grid(row=11, column=1, sticky="nesw", pady=5)

        self.lbl_ruleB = ttk.Label(master=self.frameA, text="B → ")
        self.ent_ruleB = ttk.Entry(master=self.frameA)
        self.ent_ruleB.insert(0, 'BA')
        self.lbl_ruleB.grid(row=12, column=0, sticky="e", pady=5)
        self.ent_ruleB.grid(row=12, column=1, sticky="nesw", pady=5)
        
        # Axiom
        self.lbl_axm = ttk.Label(master=self.frameA, text="Initial \nConditions", justify=tk.RIGHT)
        self.ent_axm = ttk.Entry(master=self.frameA)
        self.ent_axm.insert(0, 'A+[A]B-')
        self.lbl_axm.grid(row=13, column=0, sticky="e", pady=5)
        self.ent_axm.grid(row=13, column=1, sticky="nesw", pady=5)
        
        # Go button
        self.btn_go = ttk.Button(master=self.frameA, text="Go!", command=self.execute, style="Accent.TButton")
        self.btn_go.grid(row=14, column=1, columnspan=2, sticky="nesw", pady=10)

    def create_turtle_screen(self): ## $$
        """
        Function initializing turtle screen
        """
        # Parent frame
        self.Parent = tk.Frame(highlightbackground='yellow', highlightthickness=2)
        self.Parent.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.Parent.grid_columnconfigure(0, weight=1)
        self.Parent.grid_rowconfigure(0, weight=1, uniform="group1")
        self.Parent.grid_rowconfigure(1, weight=1, uniform="group1")

        # Top frame
        self.frameB = tk.Frame(self.Parent, highlightbackground='yellow', highlightthickness=1)
        self.frameB.grid(sticky='NESW', padx=5, pady=5)
        self.canvas = tk.Canvas(master=self.frameB)
        self.canvas.config(width=350, height=200)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")

        self.my_spicy_turtle = turtle.RawTurtle(self.screen, shape="turtle", visible=True)

        # Bottom Frame
        self.frameC = tk.Frame(self.Parent, highlightbackground='green', highlightthickness=1)
        self.frameC.grid(sticky='NESW', padx=5, pady=5)
        self.canvasC = tk.Canvas(master=self.frameC)
        self.canvasC.config(width=350, height=200)
        self.canvasC.pack(fill=tk.BOTH, expand=tk.YES)
        self.screenC = turtle.TurtleScreen(self.canvasC)
        self.screenC.bgcolor("white")
        self.my_ginger_turtle = turtle.RawTurtle(self.screenC, shape="turtle", visible=True)
        self.my_posh_turtle = turtle.RawTurtle(self.screenC, shape="turtle", visible=True)
        self.my_baby_turtle = turtle.RawTurtle(self.screenC, shape="turtle", visible=True)
        self.my_scary_turtle = turtle.RawTurtle(self.screenC, shape="turtle", visible=True)
        self.my_sporty_turtle = turtle.RawTurtle(self.screenC, shape="turtle", visible=True)


    def draw(self, s, length, angle, stack_depth, turtle_name):
        '''
        Either animates the turtle across the canvas
        or (if self.screen.tracer is switched on and off) 
        immediately outputs final image.
        '''
        
        self.screenC.tracer(False)
            
        stack = []
        for character in s:
            penwidth = 5/(0.6*len(stack)+1)
            turtle_name.pensize(width=penwidth)
            turtle_name.pencolor(0, min(1, len(stack)/(stack_depth+1)), 0.4) # takes r,g,b values from 0 to 1

            if character in string.ascii_letters:
                turtle_name.forward(length)
            elif character == '-':
                turtle_name.left(angle)
            elif character == '+':
                turtle_name.right(angle)
            elif character == '[':
                pos = turtle_name.position()
                head = turtle_name.heading()
                stack.append((pos, head))
            elif character == ']':
                prior_position, prior_heading = stack.pop()
                turtle_name.penup()
                turtle_name.goto(prior_position)
                turtle_name.setheading(prior_heading)
                turtle_name.pendown()
        
        self.screenC.tracer(True)
        
        turtle_name.penup()
    
    def execute(self):

        """ Function generating string based on user inputs
        """
        angle = float(self.ent_angle.get())
        length = float(self.ent_length.get())
        max_iter = int(self.scl_iters.get())
        A_rule = self.ent_ruleA.get()
        B_rule = self.ent_ruleB.get()
        axiom = self.ent_axm.get()

        spicy_turtles = [self.my_ginger_turtle,
                         self.my_scary_turtle,
                         self.my_posh_turtle,
                         self.my_baby_turtle,
                         self.my_sporty_turtle,
                         self.my_spicy_turtle]
        # draw based values
        for turt in spicy_turtles:
            self.reset_turtle(turt)
            turt.clear()

        canv_width = self.frameB.winfo_width() ## $$
        canv_height = self.frameB.winfo_height()
        print(canv_width, canv_height)
        self.canvas.config(width=canv_width, height=canv_height)
        self.canvasC.config(width=canv_width, height=canv_height)

        canv_height = self.canvas.winfo_height()

        # Bottom Canvas
        offset = linspace(canv_width, max_iter)
        print(offset)
        for i in range(max_iter):
            spicy_turtles[i].goto(x=.5*canv_width+offset[i], y=-0.6*canv_height)
            inp_string = generate(axiom, i+1,  A_rule, B_rule)
            self.draw(inp_string, length, angle, maxDepth(inp_string), spicy_turtles[i])

        # Top Canvas
        inp_string = generate(axiom, max_iter,  A_rule, B_rule)

        self.my_spicy_turtle.goto(x=0.5*canv_width, y=-0.6*canv_height)
        self.draw(inp_string, length, angle, maxDepth(inp_string), self.my_spicy_turtle)


    def reset_turtle(self, turtle_name):
        turtle_name.penup()
        # turtle_name.hideturtle()
        turtle_name.speed("fastest")
        turtle_name.pensize(width=3)
        turtle_name.goto(x=0, y=-0.6*self.frameB.winfo_height())
        turtle_name.setheading(90)
        
    def preset_autofill(self, args):
        
        preset_name = str(self.clicked.get())
        
        # Remove old values from entries
        self.ent_angle.delete(0, tk.END)
        self.ent_length.delete(0, tk.END)
        self.ent_ruleA.delete(0, tk.END)
        self.ent_ruleB.delete(0, tk.END)
        self.ent_axm.delete(0, tk.END)
 
        # add preset values from preset dictionary
        presets = preset_dict[preset_name]
        self.ent_angle.insert(0, presets['angle'])
        self.ent_length.insert(0, presets['length'])
        self.scl_iters.set(presets['max_iter'])
        self.ent_ruleA.insert(0, presets['ruleA'])
        self.ent_ruleB.insert(0, presets['ruleB'])
        self.ent_axm.insert(0, presets['axiom'])


def maxDepth(inp_string):
    depthCount = 0
    maxCount = 0
    for character in inp_string:
        if character == '[':
            depthCount += 1
        elif character == ']':
            depthCount -= 1
        if depthCount > maxCount:
            maxCount = depthCount
    return maxCount


def generate(string, max_iter, A_rule, B_rule):
    for step in range(max_iter):
        string = reproduce(string, A_rule, B_rule)
    return string


def reproduce(string, A_rule, B_rule):
    new = ''
    for character in string:
        if character == 'A':
            new += A_rule
        elif character == 'B':
            new += B_rule
        else:
            new += character
    return new


def linspace(canv_dim, max_iter): ## $$
    padding = 0.2
    if max_iter < 2:
        return [0]
    else:
        a = -0.5*canv_dim + padding*canv_dim
        b = 0.5*canv_dim - padding*canv_dim
        diff = (b-a)/(max_iter-1)
        return [diff*i + a for i in range(max_iter)]

preset_dict = {'Custom':   {'angle': 12,
                            'length': 10,
                            'max_iter': 2,
                            'ruleA': 'B+[[A]-A]-B[-BA]+A',
                            'ruleB': 'BA',
                            'axiom': 'A+[A]B-'},
                'Tree':    {'angle': 32,
                            'length': 20,
                            'max_iter': 4,
                            'ruleA': 'B+[[A]-A]-B[-BA]+A',
                            'ruleB': 'BA',
                            'axiom': 'A+[A]B-'},
                'Algea':   {'angle': 22.5, 
                            'length': 10,
                            'max_iter': 4,
                            'ruleA': 'AA-[-A+A+A]+[+A-A-A]',
                            'ruleB': 'B',
                            'axiom': 'A',
                            'start_color': (0, 0.6, 0.3),
                            'final_color': (0.6, 1, 1)},
                'Wheat':   {'angle': 10, 
                            'length': 10,
                            'max_iter': 4,
                            'ruleA': 'B[[+A]+B][[-A]-B]',
                            'ruleB': 'A[+B][-B]',
                            'axiom': 'AB',
                            'start_color': (0.8, 0.4, 0),
                            'final_color': (1, 1, 0.6)},
                'Bush':    {'angle': 25,
                            'length': 10,
                            'max_iter': 5,
                            'ruleA': 'A[-A][+[+A]][-[-A]]',
                            'ruleB': 'B[-B][+[+A]][-[-B]]',
                            'axiom': 'AB',
                            'start_color': (0.6, 0.3, 0),
                            'final_color': (0.4, 1, 0.4)}
}


if __name__ == '__main__':
    root = tk.Tk()
    # Set theme and font
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "dark")
    root.option_add('*Font', 'Helvetica 10')
    app = App(root)
    root.mainloop()