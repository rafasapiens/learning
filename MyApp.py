from tkinter import *

class MyApp:
   
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.my_menu = Menu(parent)
        # Adding Menubar in the widget
        self.menu_bar = Menu(root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        # all file menu-items will be added here next
        self.menu_bar.add_cascade(label='File', Menu=self.file_menu)
        root.config(Menu=self.menu_bar)


        
        self.button1 = Button(self.myContainer1)
        self.button1.configure(text="OK", background= "green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force() ### (0)
        self.button1.bind("<Return>", self.button1Click)
        self.button1.bind("<Return>", self.button1Click) ### (1)

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Cancel", background="red")
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Return>", self.button2Click)
        self.button2.bind("<Return>", self.button2Click) ### (2)

    def button1Click(self, event):
        report_event(event) ### (3)
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
    def button2Click(self, event):
        report_event(event) ### (4)
        self.myParent.destroy()

    def report_event(event): ### (5)
        """Imprime a descrição de um evento, baseado em seus atributos."""
        event_name = {"2": "KeyPress", "4": "ButtonPress"}
        print ("Time:"), str(event.time) ### (6)
        print ("EventType=") + str(event.type), \
            event_name[str(event.type)],\
            "EventWidgetId=" + str(event.widget), \
            "EventKeySymbol=" + str(event.keysym)
        my_menu = Menu(parent, **options)
        
root = Tk()
root.title("Programa PPRA 1.0")
root.geometry("400x300")
myapp = MyApp(root)
root.mainloop()
