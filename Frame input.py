from tkinter import *
root = Tk()
Label(root, text='Click em diferentes\n locais na tela abaixo').pack()
def callback(event):
    dir(event)
    ['__doc__', '__module__', 'char', 'delta', 'height', 'keycode',
'keysym', 'keysym_num', 'num', 'send_event', 'serial', 'state',
'time', 'type', 'widget', 'width', 'x', 'x_root', 'y', 'y_root']
    print ("you clicked at"), event.x, event.y
frame = Frame(root, bg='khaki', width=130, height=80)
frame.bind("<Button-1>", callback)
frame.pack()
root.geometry('400x400')
root.mainloop()
