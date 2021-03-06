try:
    import tkinter
except ImportError:
    import tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindowPadding = 8
mainWindow.title("Calculator")
mainWindow.geometry('640x480+8+400')
mainWindow['padx'] = mainWindowPadding


# display
calc = tkinter.Entry(mainWindow)
calc.grid(row=0, column=0, sticky='nsew')
calc.config(border=2, relief='ridge')

# keypad
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

# buttons
keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

# editing

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, calc.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding, calc.winfo_height() + keyPad.winfo_height())


mainWindow.mainloop()