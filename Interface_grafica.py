#Always look on the bright side of life

from tkinter import *
class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Clique aqui", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        label1.grid(sticky=E)
        label2.grid(sticky=E)

        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)

        checkbutton.grid(columnspan=2, sticky=W)

        image.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)

        button1.grid(row=2, column=2)
        button2.grid(row=2, column=3)
    def say_hi(self):
        print ("Oi, vc clicou!")

       

root = Tk()
root.geometry("400x400")
root.title('Interface gráfica')

app = App(root)
root.mainloop()
root.destroy()
