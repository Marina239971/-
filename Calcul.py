import tkinter
from tkinter import *
def q():
    return c.set(c.get() + '1')
def w():
    return c.set(c.get() + '+')
def e():
    return c.set(c.get() + '2')
def r():
    return c.set(c.get() + '3')
def t():
    return c.set(c.get() + '4')
def y():
    return c.set(c.get() + '5')
def u():
    return c.set(c.get() + '6')
def i():
    return c.set(c.get() + '7')
def o():
    return c.set(c.get() + '8')
def p():
    return c.set(c.get() + '9')
def a():
    return c.set(c.get() + '-')
def s():
    return c.set(c.get() + '**')
def z():
    return c.set(c.get() + '(')
def x():
    return c.set(c.get() + ')')
def d():
    return c.set(c.get() + '*')
def h():
    return c.set('')
def j():
    return c.set(c.get() + '/')
def ravn():
    return c.set(eval(c.get()))

window = Tk()
window.title("Калькулятор")
window.geometry('270x245')
c = StringVar()
knopka1 = tkinter.Button(window, text = "1",command = q,font = 'Arial 25')
knopka1.place(x=0,y=50)
knopka2 = tkinter.Button(window, text = "2",command = e,font = 'Arial 25')
knopka2.place(x=45,y=50)
knopka3 = tkinter.Button(window, text = "3",command = r,font = 'Arial 25')
knopka3.place(x=90,y=50)
knopka4 = tkinter.Button(window, text = "4",command = t,font = 'Arial 25')
knopka4.place(x=0,y=115)
knopka5 = tkinter.Button(window, text = "5",command = y,font = 'Arial 25')
knopka5.place(x=45,y=115)
knopka6 = tkinter.Button(window, text = "6",command = u,font = 'Arial 25')
knopka6.place(x=90,y=115)
knopka7 = tkinter.Button(window, text = "7",command = i,font = 'Arial 25')
knopka7.place(x=0,y=180)
knopka8 = tkinter.Button(window, text = "8",command = o,font = 'Arial 25')
knopka8.place(x=45,y=180)
knopka9 = tkinter.Button(window, text = "9",command = p,font = 'Arial 25')
knopka9.place(x=90,y=180)
knopka10 = tkinter.Button(window, text = "=",command = ravn,font = 'Arial 25')
knopka10.place(x=135,y=50)
knopka11 = tkinter.Button(window, text = "+",command = w,font = 'Arial 25')
knopka11.place(x=135,y=115)
knopka12 = tkinter.Button(window, text = "-",command = a,font = 'Arial 25')
knopka12.place(x=135,y=180)
knopka13 = tkinter.Button(window, text = "*",command = d,font = 'Arial 25')
knopka13.place(x=180,y=50)
knopka14 = tkinter.Button(window, text = "/",command = j,font = 'Arial 25')
knopka14.place(x=180,y=115)
knopka15 = tkinter.Button(window, text = "(",command = z,font = 'Arial 25')
knopka15.place(x=173,y=180)
knopka15 = tkinter.Button(window, text = ")",command = x,font = 'Arial 25')
knopka15.place(x=211,y=180)
knopka16 = tkinter.Button(window, text = "с",command = h,font = 'Arial 25')
knopka16.place(x=220,y=50)
knopka17 = tkinter.Button(window, text = "**",command = s,font = 'Arial 25')
knopka17.place(x=215,y=115)
pole = tkinter.Entry(window,width =40, textvariable = c)
pole.place(x=15,y=10)
window.mainloop()