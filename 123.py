from tkinter import *

root = Tk()

e1 = Entry(width=20)
e2 = Entry(width=20)
p = Button(text="+")
m1 = Button(text="-")
m2 = Button(text="*")
d = Button(text="/")
l = Label(width=20, fg='black')

def f():
  a = e1.get()
  return int(a)


def g():
  b = e2.get()
  return int(b)


def p1(event):
  c = f()+g()
  c = str(c)
  l['text'] = ' '.join(c)

def m11(event):
c = f()-g()
c = str(c)
l['text'] = ' '.join(c)

def m21(event):
  c = f()*g()
  c = str(c)
  l['text'] = ' '.join(c)

def d1(event):
  c = f()/g()
  c = str(c)
  l['text'] = ' '.join(c)


p.bind('<Button-1>', p1)
m1.bind('<Button-1>', m11)
m2.bind('<Button-1>', m21)
d.bind('<Button-1>', d1)

e1.pack()
e2.pack()
p.pack()
m1.pack()
m2.pack()
d.pack()
l.pack()

root.mainloop()
