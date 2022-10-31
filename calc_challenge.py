try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()
mainWindowPadding = 8
mainWindow.title("Calculator")
mainWindow.geometry('480x640')
mainWindow['padx'] = mainWindowPadding
mainWindow['pady'] = mainWindowPadding

label = tkinter.Label(mainWindow, text="Calculator", font=50)
label.grid(row=0, column=1, columnspan=2)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=2)
mainWindow.rowconfigure(2, weight=6)

# screen
result = tkinter.Entry(mainWindow)
result.grid(row=1, column=0, columnspan=4, sticky='nsew')

# Keypad
keypad = tkinter.Frame(mainWindow)
keypad.grid(row=2, column=0, columnspan=4, sticky='news')

keypad.columnconfigure(0, weight=1)
keypad.columnconfigure(1, weight=1)
keypad.columnconfigure(2, weight=1)
keypad.columnconfigure(3, weight=1)

keypad.rowconfigure(0, weight=1)
keypad.rowconfigure(1, weight=1)
keypad.rowconfigure(2, weight=1)
keypad.rowconfigure(3, weight=1)
keypad.rowconfigure(4, weight=1)


# Buttons
Bc = tkinter.Button(keypad, text="C", font=80)
Bc.grid(row=0, column=0, sticky='nsew')

Bce = tkinter.Button(keypad, text="CE", font=80)
Bce.grid(row=0, column=1, sticky='nsew')

B1 = tkinter.Button(keypad, text="1", font=80)
B1.grid(row=3, column=0, sticky='nsew')

B2 = tkinter.Button(keypad, text="2", font=80)
B2.grid(row=3, column=1, sticky='nsew')

B3 = tkinter.Button(keypad, text="3", font=80)
B3.grid(row=3, column=2, sticky='nsew')

B4 = tkinter.Button(keypad, text="4", font=80)
B4.grid(row=2, column=0, sticky='nsew')

B5 = tkinter.Button(keypad, text="5", font=80)
B5.grid(row=2, column=1, sticky='nsew')

B6 = tkinter.Button(keypad, text="6", font=80)
B6.grid(row=2, column=2, sticky='nsew')

B7 = tkinter.Button(keypad, text="7", font=80)
B7.grid(row=1, column=0, sticky='nsew')

B8 = tkinter.Button(keypad, text="8", font=80)
B8.grid(row=1, column=1, sticky='nsew')

B9 = tkinter.Button(keypad, text="9", font=80)
B9.grid(row=1, column=2, sticky='nsew')

B0 = tkinter.Button(keypad, text="0", font=80)
B0.grid(row=4, column=0, sticky='nsew')

Bmin = tkinter.Button(keypad, text="-", font=80)
Bmin.grid(row=2, column=3, sticky='nsew')

Bplus = tkinter.Button(keypad, text="+", font=80)
Bplus.grid(row=1, column=3, sticky='nsew')

Bmult = tkinter.Button(keypad, text="*", font=80)
Bmult.grid(row=3, column=3, sticky='nsew')

Bdiv = tkinter.Button(keypad, text="/", font=80)
Bdiv.grid(row=4, column=3, sticky='nsew')

Beq = tkinter.Button(keypad, text="=", font=80)
Beq.grid(row=4, column=1, columnspan=2, sticky='nsew')

Bsmax = tkinter.Button(keypad, text="Bruh", font=80)
Bsmax.grid(row=0, column=2, columnspan=2, sticky='nsew')

mainWindow.update()
mainWindow.minsize(keypad.winfo_width() - 100 + mainWindowPadding, result.winfo_height() - 100 + keypad.winfo_height())
mainWindow.maxsize(keypad.winfo_width() + 50 + mainWindowPadding, result.winfo_height() + 50 + keypad.winfo_height())

mainWindow.mainloop()
