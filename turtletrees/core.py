import tkinter as tk

window = tk.Tk()

# Create LHS frame for inputs
frm_input = tk.Frame(master=window)

frm_entry = tk.Frame(master=frm_input)

lbl_angle = tk.Label(master=frm_entry, text="Angle: ")
lbl_angle.pack(side=tk.LEFT)

ent_angle = tk.Entry(master=frm_entry, textvariable=10)
ent_angle.pack(side=tk.RIGHT)

frm_entry.pack(fill=tk.BOTH, expand=tk.YES)

frm_input.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)

frm_output = tk.Frame(master=window)
frm_output.pack(fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)

window.mainloop()
