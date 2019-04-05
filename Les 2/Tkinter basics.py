from tkinter import *
import tkinter as tk

def clicked():
    label['text'] = entry.get()

root = Tk()

label = Label(master=root,
              text='Thuisbioscoop',
              background='black',
              foreground='pink',
              font=('Century Gothic', 14, 'bold italic'),
              width=22,
              height=3)
label.pack()

button1 = Button(master=root, text='Film: Before I fall, aangeboden door: Yin', bg='light blue', command=clicked)
button1.pack(pady=10)

button2 = Button(master=root, text='Film: Irreplaceable you, aangeboden door: Waad', bg='pink', command=clicked)
button2.pack(pady=10)

button3 = Button(master=root, text='Film: Turn up Charlie, aangeboden door: Ashni', bg='light blue', command=clicked)
button3.pack(pady=10)

button4 = Button(master=root, text="Film: Isn't it romantic, aangeboden door: Qiang", bg='pink', command=clicked)
button4.pack(pady=10)

button5 = Button(master=root, text='Film: Bird box, aangeboden door: Kevin', bg='light blue', command=clicked)
button5.pack(pady=10)

button6 = Button(master=root, text='Film: Mowgli, aangeboden door: Milot', bg='pink', command=clicked)
button6.pack(pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

import datetime
d=datetime.date(2019, 3, 27)
print(d)
root.mainloop()