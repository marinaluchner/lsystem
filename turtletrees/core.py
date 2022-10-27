import turtle
import string
from tkinter import StringVar, ttk
import tkinter as tk


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
    #   self.preset_values()


    def create_widgets(self):
        
        """Function creating and arranging widgets in left panel
        """
        
        self.frameA = tk.Frame()
        self.frameA.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)
        self.frameA.columnconfigure([0, 1], minsize=40)
        self.frameA.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], minsize=20) 
        
        
        # # Preselection list
        clicked = StringVar()
        clicked.set( "Custom" )
        options = ["Tree", "Custom"]
        self.axiom_label = tk.Label(master=self.frameA, text="Select an organic structure")
        self.axiom_label.grid(row=1, column=1, columnspan=2, sticky="nesw")
        self.preselects = tk.OptionMenu(self.frameA, clicked, *options)
        self.preselects.grid(row=2, column=1,columnspan=2, sticky="nesw")
        
        # angle input
        self.lbl_angle = tk.Label(master=self.frameA, text="Angle: ")
        self.ent_angle = tk.Entry(master=self.frameA)
        self.ent_angle.insert(0, '20')
        self.lbl_angle.grid(row=3, column=0, sticky="e")
        self.ent_angle.grid(row=3, column=1, sticky="nesw")
        
        # length input
        self.lbl_length = tk.Label(master=self.frameA, text="Length: ")
        self.ent_length = tk.Entry(master=self.frameA)
        self.ent_length.insert(0, '15')
        self.lbl_length.grid(row=4, column=0, sticky="e")
        self.ent_length.grid(row=4, column=1, sticky="nesw")
        
        # iteractions slider
        self.lbl_iters = tk.Label(master=self.frameA, text="Iterations: ")
        self.scl_iters = tk.Scale(master=self.frameA, from_=0, to=5, orient=tk.HORIZONTAL)
        self.lbl_iters.grid(row=5, column=0, sticky="e")
        self.scl_iters.grid(row=5, column=1, sticky="nesw")
        
        # reproduction rules
        
        self.rep_label = tk.Label(master=self.frameA, text="Reproduction Rules")
        self.rep_label.grid(row=6, column=1,columnspan=2, sticky="nesw")
        
        self.lbl_ruleA = tk.Label(master=self.frameA, text="A ->")
        self.ent_ruleA = tk.Entry(master=self.frameA)
        self.ent_ruleA.insert(0,'B+[[A]-A]-B[-BA]+A')
        self.lbl_ruleA.grid(row=7, column=0, sticky="e")
        self.ent_ruleA.grid(row=7, column=1, sticky="nesw")
        
        self.lbl_ruleB = tk.Label(master=self.frameA, text="B ->")
        self.ent_ruleB = tk.Entry(master=self.frameA)
        self.ent_ruleB.insert(0,'BA')
        self.lbl_ruleB.grid(row=8, column=0, sticky="e")
        self.ent_ruleB.grid(row=8, column=1, sticky="nesw")
        
        # Axiom 
        self.lbl_axm = tk.Label(master=self.frameA, text="Initial Conditions")
        self.ent_axm  = tk.Entry(master=self.frameA)
        self.ent_axm.insert(0,'A+[A]B-')
        self.lbl_axm.grid(row=9, column=0, sticky="e")
        self.ent_axm.grid(row=9, column=1, sticky="nesw")
        
        # Go button
        self.btn_go = tk.Button(master=self.frameA, text="Go!", command=self.execute)
        self.btn_go.grid(row=12, column=1, columnspan=2, sticky="nesw")
    
    
    def create_turtle_screen(self):
        
        """Function initializing turtle screen
        """

        self.frameB = tk.Frame()
        self.frameB.pack(fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
        
        self.canvas = tk.Canvas(master=self.frameB)
        self.canvas.config(width=600, height=500)
        self.canvas.pack(expand=tk.YES)
        
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("black")
        
        self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.reset_turtle()
    
    def draw(self, s, length, angle, stack_depth):
        '''
        Either animates the turtle across the canvas
        or (if self.screen.tracer is switched on and off) 
        immediately outputs final image.
        '''
        self.reset_turtle()
        #values = {"x_start_position": 0, "y_start_position": -200, "color": "white", "speed": 0, "pensize": 3 , "heading": 9}
        #self.autofill_turtle(values)

        self.screen.tracer(False)

        stack = []
        for character in s:
            penwidth = 5/(0.6*len(stack)+1)
            self.my_lovely_turtle.pensize(width=penwidth)
            self.my_lovely_turtle.pencolor(0, min(1, len(stack)/(stack_depth+1)), 0.4) # takes r,g,b values from 0 to 1

            if character in string.ascii_letters:
                self.my_lovely_turtle.forward(length)
            elif character == '-':
                self.my_lovely_turtle.left(angle)
            elif character == '+':
                self.my_lovely_turtle.right(angle)
            elif character == '[':
                pos = self.my_lovely_turtle.position()
                head = self.my_lovely_turtle.heading()
                stack.append((pos, head))
            elif character == ']':
                prior_position, prior_heading = stack.pop()
                self.my_lovely_turtle.penup()
                self.my_lovely_turtle.goto(prior_position)
                self.my_lovely_turtle.setheading(prior_heading)
                self.my_lovely_turtle.pendown()

        self.screen.tracer(True)

    
    def execute(self):

        """ Function generating string based on user inputs
        """
        ############## depend on system
        preset_name = str(self.clicked.get())
        print(preset_name)
        if preset_name == 'Custom':
            
            angle = float(self.ent_angle.get())
            length = float(self.ent_length.get())
            max_iter = int(self.scl_iters.get())
            A_rule = self.ent_ruleA.get()
            B_rule = self.ent_ruleA.get()
            axiom =  self.ent_axm.get()
       
        else:
            
            angle = preset_dict[preset_name]['angle']
            length = preset_dict[preset_name]['length']
            max_iter = preset_dict[preset_name]['max_iter']
            A_rule = preset_dict[preset_name]['ruleA']
            B_rule = preset_dict[preset_name]['ruleB']
            axiom =  preset_dict[preset_name]['axiom']
            
            self.ent_angle.insert(0,angle)
            self.ent_scl_iters.insert(0,length)
            self.ent_ruleA.insert(0,max_iter)
            self.ent_ruleA.insert(0,A_rule)
            self.ent_ruleB.insert(0,B_rule)
            self.ent_axm.insert(0,axiom)
        
        # preset_val = self.clicked.get()
        # angle = float(self.ent_angle.get())
        # length = float(self.ent_length.get())
        # max_iter = int(self.scl_iters.get())
        # A_rule = self.ent_ruleA.get()
        # B_rule = self.ent_ruleA.get()
        # axiom = self.ent_axm.get()
            
        inp_string = generate(axiom, max_iter,  A_rule, B_rule)
        self.draw(inp_string, length, angle, maxDepth(inp_string))
    
    def reset_turtle(self):
        self.my_lovely_turtle.reset()
        #self.my_lovely_turtle.hideturtle()
        self.my_lovely_turtle.penup()
        self.my_lovely_turtle.goto(x=0, y=-200)
        self.my_lovely_turtle.color("white")
        self.my_lovely_turtle.speed("fastest")
        self.my_lovely_turtle.pensize(width=3)
        self.my_lovely_turtle.setheading(90)
    
    # def preset_values(self, preset_choice):
    #     self.ent_angle.insert(0, preset_dict[preset_choice]['angle'])
    #     self.ent_length.insert(0,preset_dict[preset_choice]['length'])
    #     self.scl_iters.insert(0,preset_dict[preset_choice]['max_iter'])
    #     self.ent_ruleA.insert(0,preset_dict[preset_choice]['ruleA'])
    #     self.ent_ruleB.insert(0,preset_dict[preset_choice]['ruleB'])
    #     self.ent_axm.insert(0,preset_dict[preset_choice]['axiom'])
    

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


preset_dict = {
              'Tree': {'angle': 32, 
                        'length': 20, 
                        'max_iter': 4,
                        'ruleA': 'B+[[A]-A]-B[-BA]+A' ,
                        'ruleB': 'BA',
                        'axiom':'A+[A]B-'}
              }


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
