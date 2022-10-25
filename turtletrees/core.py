import tkinter as tk
import turtle
import string

# From George and Marina
# def generator(iter_max, axioms)


def draw(inp_string):
    """
    Draws the given string.

    Parameters
    ----------
    inp_string : str
        The string to draw.
    """

    turtle = my_lovely_turtle
    turtle.reset()
    angle = float(ent_angle.get())
    length = float(ent_length.get())
    """ TODO: documentation """
    for c in inp_string:
        if c in string.ascii_letters:
            turtle.forward(length)
        elif c == '-':
            turtle.left(angle)
        elif c == '+':
            turtle.right(angle)


def execute():
    """
    Executes the program.
    """
    # inp_string = generator()
    inp_string = 'AAA++A-A-A-A'
    draw(inp_string)


window = tk.Tk()

# Could automatically generate many widgets using a dictionary

# Create LHS frame for inputs
frm_input = tk.Frame(master=window,)

# Create angle input
frm_angle = tk.Frame(master=frm_input)
lbl_angle = tk.Label(master=frm_angle, text="Angle: ")
lbl_angle.pack(side=tk.LEFT)
ent_angle = tk.Entry(master=frm_angle)
ent_angle.insert(0, '10')
ent_angle.pack(side=tk.RIGHT)
frm_angle.pack(fill=tk.BOTH, expand=tk.YES)

# Create length input
frm_length = tk.Frame(master=frm_input)
lbl_length = tk.Label(master=frm_length, text="Length: ")
lbl_length.pack(side=tk.LEFT)
ent_length = tk.Entry(master=frm_length)
ent_length.insert(0, '5')
ent_length.pack(side=tk.RIGHT)
frm_length.pack(fill=tk.BOTH, expand=tk.YES)

# Create iterations slider
frm_iters = tk.Frame(master=frm_input)
lbl_iters = tk.Label(master=frm_iters, text="Iterations: ")
lbl_iters.pack(side=tk.LEFT)
scl_iters = tk.Scale(master=frm_iters, from_=0, to=5, orient=tk.HORIZONTAL)
scl_iters.pack(side=tk.RIGHT)
frm_iters.pack(fill=tk.BOTH, expand=tk.YES)

# Create Go button
# frm_go = tk.Frame(master=frm_input)
btn_go = tk.Button(master=frm_input, text="Go!", command=execute)
btn_go.pack()

frm_input.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)

# Create output frame 
frm_output = tk.Frame(master=window)

canvas = tk.Canvas(master=frm_output)
canvas.config()
canvas.pack()
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("cyan")
frm_output.pack(fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")

# TODO: Set initial window size as minimum size


window.mainloop()
