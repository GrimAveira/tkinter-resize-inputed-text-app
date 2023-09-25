from tkinter import *

class MyApp():
    def __init__(self):
        self.root = Tk()
        self.root.title("METANIT.COM")
        self.root.geometry("850x850")
        self.fontSize=10
        self.message = StringVar()
        self.xLabel=Label(text="Координата x")
        self.xLabel.pack()
        self.xEntry = Entry(width=20)
        self.xEntry.pack()
        self.yLabel=Label(text="Координата y")
        self.yLabel.pack()
        self.yEntry = Entry(width=20)
        self.yEntry.pack()
        self.accept=Button(self.root, text="Применить координаты", command=self.acceptCord)
        self.accept.pack()
        self.textLabel=Label(text="Выводимый текст")
        self.textLabel.pack()
        self.text = Entry(width=20, textvariable=self.message)
        self.text.pack()
        self.labelOut = Label(self.root, borderwidth=1, relief="solid")
        self.labelOut.pack(padx=0, pady=0,anchor='nw')
        self.label = Label(self.labelOut, textvariable=self.message, borderwidth=1, relief="solid",
            font='Times 10')
        self.label.pack(padx=5, pady=5)
        self.root.bind('<Key>',self.keypress)
    def playApp(self):
        self.root.mainloop()
    def keypress(self, event):
        self.fontSize
        if event.keycode==27:
            self.root.destroy()
        if event.keycode==37:
            self.fontSize/=2
            self.label['font']= 'Times '+str(int(self.fontSize))
        if event.keycode==39:
            self.fontSize*=2
            self.label['font']= 'Times '+str(int(self.fontSize))
    def acceptCord(self):
        self.labelOut.pack(padx=self.xEntry.get(), pady=self.yEntry.get(),anchor='nw')

app=MyApp()
app.playApp()