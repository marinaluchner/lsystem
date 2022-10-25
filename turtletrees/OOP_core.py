import turtle
import tkinter as tk
import string

class App:
    def __init__(self, master):
        
        """_summary_
        """
        self.master = master
        self.master.title("Raw Turtle")
 
        self.create_widgets()
        self.create_turtle_screen()
        
    
    def create_widgets(self):
        
        """_summary_
        """
        
        self.frameA = tk.Frame()
        self.frameA.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)
        self.frameA.columnconfigure([0, 1], minsize=20)
        self.frameA.rowconfigure([0, 1, 2], minsize=20) 
        
        # angle input
        self.lbl_angle = tk.Label(master=self.frameA, text="Angle: ")
        self.ent_angle = tk.Entry(master=self.frameA)
        self.ent_angle.insert(0, '10')
        self.lbl_angle.grid(row=0, column=0, sticky="nesw")
        self.ent_angle.grid(row=0, column=1, sticky="nesw")
        
        # length input
        self.lbl_length = tk.Label(master=self.frameA, text="Length: ")
        self.ent_length = tk.Entry(master=self.frameA)
        self.ent_length.insert(0, '5')
        self.lbl_length.grid(row=1, column=0, sticky="nesw")
        self.ent_length.grid(row=1, column=1, sticky="nesw")
        
        # iteractions slider
        self.lbl_iters = tk.Label(master=self.frameA, text="Iterations: ")
        self.scl_iters = tk.Scale(master=self.frameA, from_=0, to=5, orient=tk.HORIZONTAL)
        self.lbl_iters .grid(row=2, column=0, sticky="nesw")
        self.scl_iters .grid(row=2, column=1, sticky="nesw")
        
        # Go button
        self.btn_go = tk.Button(master=self.frameA, text="Go!", command=self.execute)
        self.btn_go.grid(row=3, column=1, sticky="nesw")
    
    def create_turtle_screen(self):
        
        """_summary_
        """
        
        self.frameB = tk.Frame()
        self.frameB.pack(fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
        
        self.canvas = tk.Canvas(master=self.frameB)
        self.canvas.config(width=600, height=500)
        self.canvas.pack(expand=tk.YES)
        
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("cyan")
        
        self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.my_lovely_turtle.color("green")
        
    def draw(self, inp_string):
        
        """_summary_
        """
        
        angle = float(self.ent_angle.get())
        length = float(self.ent_length.get())
        self.my_lovely_turtle.reset()
        for c in inp_string:
            if c in string.ascii_letters:
                self.my_lovely_turtle.forward(length)
            elif c == '-':
                self.my_lovely_turtle.left(angle)
            elif c == '+':
                self.my_lovely_turtle.right(angle)
                    

    def execute(self):
        
        """
        """
        
        inp_string = "A+B-C+E+E+E+E"
        #inp_string = generator()
        self.draw(inp_string)
    

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()