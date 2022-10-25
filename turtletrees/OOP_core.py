import turtle
import string
from tkinter import StringVar, ttk
import tkinter as tk
import lsystem
class App:
    def __init__(self, master):
        
        """Initialize class App
        
        params
        ============
        master: window
        """
        self.master = master
        self.master.title("Raw Turtle")

        self.create_widgets()
        self.create_turtle_screen()


    def create_widgets(self):
        
        """Function creating and arranging widgets in left panel
        """
        
        self.frameA = tk.Frame()
        self.frameA.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)
        self.frameA.columnconfigure([0, 1], minsize=40)
        self.frameA.rowconfigure([0, 1, 2, 3, 4, 5, 6,7,8], minsize=20) 
        
        # angle input
        self.lbl_angle = tk.Label(master=self.frameA, text="Angle: ")
        self.ent_angle = tk.Entry(master=self.frameA)
        self.ent_angle.insert(0, '20')
        self.lbl_angle.grid(row=0, column=0, sticky="nesw")
        self.ent_angle.grid(row=0, column=1, sticky="nesw")
        
        # length input
        self.lbl_length = tk.Label(master=self.frameA, text="Length: ")
        self.ent_length = tk.Entry(master=self.frameA)
        self.ent_length.insert(0, '15')
        self.lbl_length.grid(row=1, column=0, sticky="nesw")
        self.ent_length.grid(row=1, column=1, sticky="nesw")
        
        # iteractions slider
        self.lbl_iters = tk.Label(master=self.frameA, text="Iterations: ")
        self.scl_iters = tk.Scale(master=self.frameA, from_=0, to=5, orient=tk.HORIZONTAL)
        self.lbl_iters.grid(row=2, column=0, sticky="nesw")
        self.scl_iters.grid(row=2, column=1, sticky="nesw")
        
        # Preselction list
        self.axiom_label = tk.Label(master=self.frameA, text="Select an organic structure")
        self.axiom_label.grid(row=3, column=1, columnspan=2, sticky="nesw")
        self.preselects = tk.OptionMenu(self.frameA, StringVar(), "Python", "C", "C++", "Java", "Custom")
        self.preselects.grid()
        
        # Go button
        self.btn_go = tk.Button(master=self.frameA, text="Go!", command=self.execute)
        self.btn_go.grid(row=8, column=1, columnspan=2, sticky="nesw")
    
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
        

    def draw(self, s, length, angle):
        '''
        Either animates the turtle across the canvas
        or (if self.screen.tracer is switched on and off) 
        immediately outputs final image.
        '''

        self.reset_turtle()

        stack = []
        for character in s:
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
    

    def execute(self):
        
        """ Function generating string based on user inputs
        """
        angle = float(self.ent_angle.get())
        length = float(self.ent_length.get())
        max_iter = int(self.scl_iters.get())
        #axiom = 
        #inp_string = "A+B-C+E+E+E+E"

        inp_string = lsystem.generate(string = 'A+[A]B-', max_iter=max_iter)
        self.draw(inp_string, length, angle)
        
    def reset_turtle(self):
        self.my_lovely_turtle.reset()
        self.my_lovely_turtle.goto(x=0, y=-200)
        self.my_lovely_turtle.color("white")
        self.my_lovely_turtle.speed(0)
        self.my_lovely_turtle.pensize(width=3)
        self.my_lovely_turtle.setheading(90)
        
    

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()