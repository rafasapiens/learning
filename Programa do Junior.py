from tkinter import *
class App:
    def __init__(self, root, use_geometry, show_buttons):
        fm = Frame(root, width=300, height=200, bg="green")
        fm.pack(side=TOP, expand=NO, fill=NONE)
        if use_geometry:
            root.geometry("600x400")
            ### (1) observe o método gerenciador de janelas
        if show_buttons:
            Button(fm, text="Button 1", width=10).pack(side=LEFT)
            Button(fm, text="Button 2", width=10).pack(side=LEFT)
            Button(fm, text="Button 3", width=10).pack(side=LEFT)
case = 0
for use_geometry in (0, 1):
    for show_buttons in (0,1):
        case = case + 1
        root = Tk()
        root.wm_title("Case " + str(case))
        ### (2) observe o método gerenciador de janelas wm_title
        display = App(root, use_geometry, show_buttons)
        root.mainloop()
'''
from tkinter import *


root = Tk()
myContainer1 = Frame(root)
myContainer1.pack()
button1 = Button(myContainer1) ### (1)
button1["text"]= "Hello, World!" ### (2)
button1["background"] = "green" ### (3)
button1.pack() ### (4)
root.mainloop()'''
