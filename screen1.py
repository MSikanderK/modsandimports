try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 10

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

filelist = tkinter.Listbox(mainWindow)
filelist.grid(row=1, column=0, sticky='nsew', rowspan=2)
filelist.config(border=2, relief='sunken')
for zone in os.listdir('C:\Windows\System32'):
    filelist.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=filelist.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
filelist['yscrollcommand'] = listScroll.set

#frame for file detail buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

#file detail buttons
rbValue = tkinter.IntVar()
rbValue.set(0)
radio1 = tkinter.Radiobutton(optionFrame, text= 'File Name', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text= 'Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text= 'Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

#Result bar
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result =  tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

#frame for time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text=" Time")
timeFrame.grid(row=3, column=0, sticky='new')

#time spinners
hourSpinner= tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minSpinner= tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secSpinner= tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,60)))
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secSpinner.grid(row=0, column=4)
timeFrame['padx']= 36

#frame for date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

#Date labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

#day spinners
daySpinbox= tkinter.Spinbox(dateFrame, width=5, values=tuple(range(1,31)))
monSpinbox= tkinter.Spinbox(dateFrame, width=5, values = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
yearSpinbox= tkinter.Spinbox(dateFrame, width=5, values=tuple(range(2000,2099)))
daySpinbox.grid(row=1, column=0)
monSpinbox.grid(row=1, column=1)
yearSpinbox.grid(row=1, column=2)

#buttons
okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

print(rbValue.get())
