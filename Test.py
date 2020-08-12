import tkinter as tk # 1
win = tk.Tk() # 2
from tkinter import ttk # 3

win.title("Python GUI") # 3
# Adding a Label # 4
ttk.Label(win, text="A Label").grid(column=0, row=0) # 5
# Modify adding a Label # 1
aLabel = ttk.Label(win, text="A Label") # 2
aLabel.grid(column=0, row=0) # 3
# Button Click Event Callback Function # 4
def clickMe(): # 5
    action.configure(text='Hello ' + name.get())
    # Adding a Button # 6

action = ttk.Button(win, text="Click Me!", command=clickMe) # 7
action.grid(column=1, row=1) # 8

# Changing our Label # 3
ttk.Label(win, text="Enter a name:").grid(column=0, row=0) # 4
# Adding a Textbox Entry widget # 5
name = tk.StringVar() # 6
nameEntered = ttk.Entry(win, width=12, textvariable=name) # 7
nameEntered.grid(column=0, row=1) # 8
nameEntered.focus() # Place cursor into name Entry

win.mainloop() # 5

new_col_loc = (chr(int(ord(cell.coordinate[0:1])) + 4))
print(new_col_loc)
