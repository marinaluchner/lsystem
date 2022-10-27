import turtle
import string
from tkinter import StringVar, ttk
import tkinter as tk
import string


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
        self.clicked.set( "Custom" )
        
        self.create_widgets()
        self.create_turtle_screen()

    def create_widgets(self):
        
        """Function creating and arranging widgets in left panel
        """
        
        self.frameA = tk.Frame()
        self.frameA.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)
        self.frameA.columnconfigure([0, 1], minsize=40)
        self.frameA.rowconfigure(list(range(1,16)), minsize=20) 
        
        # Description 
        self.description = tk.Label(master=self.frameA, 
                                    text="Select an organic structure n\n\yes or no")
        self.description.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="w")
        
        # Preset values
        options = ["Tree", "Custom"]
        self.axiom_label = tk.Label(master=self.frameA, text="Select an organic structure")
        self.axiom_label.grid(row=5, column=1, columnspan=2, sticky="nesw")
        self.preselects = tk.OptionMenu(self.frameA, self.clicked, *options, command=self.preset_autofill)
        self.preselects.grid(row=6, column=1,columnspan=2, sticky="nesw")
        
        # angle input
        self.lbl_angle = tk.Label(master=self.frameA, text="Angle: ")
        self.ent_angle = tk.Entry(master=self.frameA)
        self.ent_angle.insert(0, '20')
        self.lbl_angle.grid(row=7, column=0, sticky="e")
        self.ent_angle.grid(row=7, column=1, sticky="nesw")
        
        # length input
        self.lbl_length = tk.Label(master=self.frameA, text="Length: ")
        self.ent_length = tk.Entry(master=self.frameA)
        self.ent_length.insert(0, '15')
        self.lbl_length.grid(row=8, column=0, sticky="e")
        self.ent_length.grid(row=8, column=1, sticky="nesw")
        
        # iteractions slider
        self.lbl_iters = tk.Label(master=self.frameA, text="Iterations: ")
        self.scl_iters = tk.Scale(master=self.frameA, from_=0, to=5, orient=tk.HORIZONTAL)
        self.lbl_iters.grid(row=9, column=0, sticky="e")
        self.scl_iters.grid(row=9, column=1, sticky="nesw")
        
        # reproduction rules
        self.rep_label = tk.Label(master=self.frameA, text="Reproduction Rules")
        self.rep_label.grid(row=10, column=1,columnspan=2, sticky="nesw")
        
        self.lbl_ruleA = tk.Label(master=self.frameA, text="A ->")
        self.ent_ruleA = tk.Entry(master=self.frameA)
        self.ent_ruleA.insert(0,'B+[[A]-A]-B[-BA]+A')
        self.lbl_ruleA.grid(row=11, column=0, sticky="e")
        self.ent_ruleA.grid(row=11, column=1, sticky="nesw")
        
        self.lbl_ruleB = tk.Label(master=self.frameA, text="B ->")
        self.ent_ruleB = tk.Entry(master=self.frameA)
        self.ent_ruleB.insert(0,'BA')
        self.lbl_ruleB.grid(row=12, column=0, sticky="e")
        self.ent_ruleB.grid(row=12, column=1, sticky="nesw")
        
        # Axiom 
        self.lbl_axm = tk.Label(master=self.frameA, text="Initial Conditions")
        self.ent_axm  = tk.Entry(master=self.frameA)
        self.ent_axm.insert(0,'A+[A]B-')
        self.lbl_axm.grid(row=13, column=0, sticky="e")
        self.ent_axm.grid(row=13, column=1, sticky="nesw")
        
        # Go button
        self.btn_go = tk.Button(master=self.frameA, text="Go!", command=self.execute)
        self.btn_go.grid(row=14, column=1, columnspan=2, sticky="nesw")
    
    
    def create_turtle_screen(self):
        
        """Function initializing turtle screen
        """
        # Parent frame
        self.Parent = tk.Frame()
        self.Parent.pack(side=tk.RIGHT, expand=tk.YES)
        self.Parent.grid_rowconfigure(0, weight=1)
        self.Parent.grid_rowconfigure(1, weight=1)

        # Top frame
        self.frameB = tk.Frame(self.Parent)
        self.frameB.grid(sticky='nsew', padx=5, pady=5)
        self.canvas = tk.Canvas(master=self.frameB)
        self.canvas.config(width=200, height=200)
        self.canvas.pack(expand=tk.YES)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("black")
        self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.reset_turtle(turtle_name=self.my_lovely_turtle)

        # Bottom Frame
        self.frameC = tk.Frame(self.Parent)
        self.frameC.grid(sticky='nsew', padx=5, pady=5)
        self.canvasC = tk.Canvas(master=self.frameC)
        self.canvasC.config(width=200, height=200)
        self.canvasC.pack(expand=tk.YES)
        self.screenC = turtle.TurtleScreen(self.canvasC)
        self.screenC.bgcolor("blue")
        self.my_bashful_turtle = turtle.RawTurtle(self.screenC, shape="turtle")
        self.reset_turtle(self.my_bashful_turtle)

    
    def draw(self, s, length, angle, stack_depth, turtle_name, animated):
        '''
        Either animates the turtle across the canvas
        or (if self.screen.tracer is switched on and off) 
        immediately outputs final image.
        '''
        self.reset_turtle(turtle_name)
        
        if not animated:
            self.screen.tracer(False)

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

        if not animated:
            self.screen.tracer(True)
    
    def execute(self):

        """ Function generating string based on user inputs
        """
        ############## get values from inputs
        angle = float(self.ent_angle.get())
        length = float(self.ent_length.get())
        max_iter = int(self.scl_iters.get())
        A_rule = self.ent_ruleA.get()
        B_rule = self.ent_ruleA.get()
        axiom =  self.ent_axm.get()
        # draw based values
        inp_string = generate(axiom, max_iter,  A_rule, B_rule)
        self.draw(inp_string, length, angle, maxDepth(inp_string), self.my_lovely_turtle, True)
        self.draw(inp_string, length, angle, maxDepth(inp_string), self.my_bashful_turtle, True)
    
    def reset_turtle(self, turtle_name):
        turtle_name.reset()
        turtle_name.penup()
        turtle_name.color("white")
        turtle_name.speed("fastest")
        turtle_name.pensize(width=3)
        turtle_name.goto(x=0, y=-100)
        turtle_name.setheading(90)
        
    def preset_autofill(self, args):
        
        preset_name = str(self.clicked.get())
        
        # Remove old values from entries
        self.ent_angle.delete(0,tk.END)
        self.ent_length.delete(0,tk.END)
        self.ent_ruleA.delete(0,tk.END)
        self.ent_ruleB.delete(0,tk.END)
        self.ent_axm.delete(0,tk.END)
 
        # add preset values from preset dictionary
        presets = preset_dict[preset_name]
        self.ent_angle.insert(0,presets['angle'])
        self.ent_length.insert(0,presets['length'])
        self.scl_iters.set(presets['max_iter'])
        self.ent_ruleA.insert(0,presets['ruleA'])
        self.ent_ruleB.insert(0,presets['ruleB'])
        self.ent_axm.insert(0,presets['axiom'])
        
def maxDepth(inp_string): 
    depthCount = 0
    maxCount = 0
    for char in inp_string:
        if char== '[':
            depthCount += 1
        elif char == ']':
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


preset_dict = {'Custom': {'angle': 32, 
                        'length': 20, 
                        'max_iter': 1,
                        'ruleA': 'B+[[A]-A]-B[-BA]+A' ,
                        'ruleB': 'BA',
                        'axiom':'A+[A]B-'},
    
              'Tree': {'angle': 32, 
                        'length': 20, 
                        'max_iter': 1,
                        'ruleA': 'B+[[A]-A]-B[-BA]+A' ,
                        'ruleB': 'BA',
                        'axiom':'A+[A]B-'}
              }


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()