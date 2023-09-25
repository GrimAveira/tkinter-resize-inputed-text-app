from tkinter import *
 

fontSize=10

root = Tk()
root.title("METANIT.COM")
root.geometry("850x850")
message = StringVar()


def keypress(event):
    global fontSize
    if event.keycode==37:
        fontSize/=2
        label['font']= 'Times '+str(int(fontSize))
    if event.keycode==39:
        fontSize*=2
        label['font']= 'Times '+str(int(fontSize))
        
def acceptCord():
    labelOut.pack(padx=xEntry.get(), pady=yEntry.get(),anchor='nw')

textLabel=Label(text="Выводимый текст")
textLabel.pack()
text = Entry(width=20, textvariable=message)
text.pack()
xLabel=Label(text="Координата x")
xLabel.pack()
xEntry = Entry(width=20)
xEntry.pack()
yLabel=Label(text="Координата y")
yLabel.pack()
yEntry = Entry(width=20)
yEntry.pack()
accept=Button(root, text="Применить координаты", command=acceptCord)
accept.pack()


root.bind('<Key>',keypress)

labelOut = Label(root, borderwidth=1, relief="solid")
labelOut.pack(padx=0, pady=0,anchor='nw')
label = Label(labelOut, textvariable=message, borderwidth=1, relief="solid",
    font='Times 10')
label.pack(padx=5, pady=5)
 
root.mainloop()