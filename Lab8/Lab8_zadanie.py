# !/usr/bin/env python
# -*- coding: utf-8 -*-
# # Zadanie1
# # Przygotuj okno skladajace sie z jednego buttonu i 3x radioButton okreslajacych podstawowe kolory.
# # Zmiana zaznaczenia radio zmienia kolor textu na przycisku. Wcisniecie przycisku powoduyje wyswietlenie dowolnego napisu.
#
# #!/usr/bin/python
#
# import Tkinter
# import tkMessageBox
# import tkSimpleDialog
# from Tkinter import *
# # top = Tkinter.Tk()
# def helloCallBack():
#     tkSimpleDialog
#     tkMessageBox.showinfo("hello Przemek")
#
# def sel():
#     selection = "You selected the option " + str(var.get())
#     label.config(text=selection)
#
# root = Tk()
#
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
# R1.pack( anchor = W )
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
# R2.pack( anchor = W )
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
# R3.pack( anchor = W)
# R4 = Button(root,text = "Wcisnij aby zobczyc wiadomosc", command = helloCallBack() )
# # tkMessageBox.showinfo("HELLO")
# # R4.pack()
#
# #
# # x = Tkinter.Button(root,text="Hello,")
# label = Label(root)
# label.pack()
# root.mainloop()
#
# # Zadanie2
#
# # Napisz prosty sekundnik odliczajacy czas do zadanego momentu. Odliczanie rozpoczyna sie po wcisnieciu przycisku START
# # kiedy czas sie skonczy odliczanie zatrzymuje sie a program wyswietla komunikat o zakonczeniu odliczania.
#
# # Zadanie3
# # Korzystajac z modulu Tkinter napisz prosty kalkulator pozwalajacy dodawac, odejmowac, mnozyc, dzielic

from Tkinter import *
from math import *

root = Tk()
top = Frame(root);
top.pack()
Label(top, text='Define f(x):').pack(side='left')

f_entry = Entry(top, width=12)
f_entry.pack(side='left')
f_entry.insert('end', 'x')

Label(top, text='  x =').pack(side='left')
x_entry = Entry(top, width=6)
x_entry.pack(side='left')
x_entry.insert('end', '0')

s_label = Label(top, width=9)


def calc(event=None):
    f_txt = f_entry.get()
    x = float(x_entry.get())
    res = eval(f_txt)
    global s_label
    s_label.configure(text='%g' % res)  # display f(x) value


x_entry.bind('<Return>', calc)
Button(top, text='  f = ', relief='flat', command=calc).pack(side='left')
s_label.pack(side='left')


def quit(event=None): root.quit()


root.bind('<q>', quit)
root.mainloop()