from tkinter import *
from tkinter import ttk


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.map = [[]]
        self.initUI()

    def initUI(self):
        self.master.title("The way")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack()
        canvas.create_line(0,0,100,100,fill = 'green', width= 10)

        canvas.pack(fill=BOTH, expand=1)

class Coordinates:

    def __init__(self):
        self.x = 0
        self.y = 0

    def Coordinates(self, x: int, y: int):
        self.x = x
        self.y = y


class Car:

    def __init__(self):
        self.loc = None

    def Car(self, loc):
        self.loc = loc

    def getLoc(self):
        return self.loc.x, self.loc.y

    def toMove(self, x, y):
        while self.loc.x != x and self.loc.y != y:
            if self.loc.x < x: self.loc.x += 1
            if self.loc.x > x: self.loc.x -= 1
            if self.loc.y < y: self.loc.y += 1
            if self.loc.y > y: self.loc.y -= 1

root = Tk()
ex = Example()
root.mainloop()