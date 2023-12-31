from tkinter import *


class MyApp():
    def __init__(self):
        self._root = Tk()
        self._root.title("tkinter-resize-inputed-text-app")
        self._root.geometry("450x450")

        self._fontSize = 10
        self._message = StringVar()

        self._textLabel = Label(text="Выводимый текст")
        self._textLabel.pack()
        self._outputText = Entry(width=20, textvariable=self._message)
        self._outputText.pack()
        self._xLabel = Label(text="Координата x")
        self._xLabel.pack()
        self._xEntry = Entry(width=20)
        self._xEntry.pack()
        self._yLabel = Label(text="Координата y")
        self._yLabel.pack()
        self._yEntry = Entry(width=20)
        self._yEntry.pack()
        self._acceptButton = Button(
            self._root, text="Применить координаты", command=self.double_apply_coordinates)
        self._acceptButton.pack()
        self._externalLabel = Label(self._root, borderwidth=1, relief="solid")
        self._externalLabel.pack(padx=0, pady=0, anchor='nw')
        self._innerLabel = Label(self._externalLabel, textvariable=self._message, borderwidth=1, relief="solid",
                                 font='Times 10')
        self._innerLabel.pack(padx=5, pady=5)

        self._root.bind('<Escape>', self.close_app)
        self._root.bind('<Key>', self.resize_font_size)

    def entry_handler(self, value):
        """Check on invalid values.

        Keyword arguments:
        self -- the mandatory default argument (default self)
        value -- the value, which will be handle on invalid values

        """
        if int(value) < 0:
            raise ValueError()

    def start_app(self):
        """Start tkinter application.

        Keyword arguments:
        self -- the mandatory default argument (default self)

        """
        self._root.mainloop()

    def close_app(self, _):
        """Destroy tkinter application.

        Keyword arguments:
        self -- the mandatory default argument (default self)

        """
        self._root.destroy()

    def resize_font_size(self, event):
        """Resize self font size according press key.

        Keyword arguments:
        self -- the mandatory default argument (default self)
        event -- the object, which is containig property "keycode" that represent key on keyboard

        """
        if event.keycode == 37:
            self._fontSize /= 2
        if event.keycode == 39:
            self._fontSize *= 2
        self._innerLabel['font'] = 'Times '+str(int(self._fontSize))

    def double_apply_coordinates(self):
        """Call apply_coordinates two times.

        Keyword arguments:
        self -- the mandatory default argument (default self)

        """
        """Only one call function apply_coordinates don't rerender text in component"""
        self.apply_coordinates()
        self.apply_coordinates()

    def apply_coordinates(self):
        """Applies the coordinates entered in the fields to the object.

        Keyword arguments:
        self -- the mandatory default argument (default self)

        """
        """Only one call function apply_coordinates don't rerender text in component"""
        try:
            x = self._xEntry.get()
            y = self._yEntry.get()
            self.entry_handler(x)
            self.entry_handler(y)
            self._externalLabel.pack(padx=x, pady=y, anchor='nw')
            self._innerLabel.pack(padx=5, pady=5)
            self._innerLabel['text'] = self._message
            self._innerLabel.update()
        except ValueError:
            print("Недопустимое значение координат")
