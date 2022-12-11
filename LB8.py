import tkinter.filedialog
from tkinter import *
from tkinter import Canvas
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askyesno
from enum import StrEnum, auto
import os


class ShapesName(StrEnum):
    Triangle = auto()
    Rectangle = auto()
    Ellipse = auto()


class MyFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, master=parent)
        self.canvas = None
        self.master = parent
        self.curdir = os.path.curdir
        self.CurShape = ShapesName.Triangle
        self.OutLineColor = '#000000'
        self.FillColor = '#000000'
        self.widgets = []
        self.MouseHist = []
        self.InitUI()
        self.BindMouse()
        self.width = 10

    def BindMouse(self):
        self.master.bind('<Button-1>', self.event_handler)

    def ChangeShape(self, newShape):
        print('ChangeShape: new Shape {}'.format(newShape))
        for shape in ShapesName:
            if shape == newShape:
                self.CurShape = shape
        self.MouseHist.clear()

    def InitUI(self):
        menubar = Menu(self.master)

        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Create file", command=self.CreateFile)
        fileMenu.add_command(label="Save File", command=self.SaveFile)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)

        ShapeMenu = Menu(menubar, tearoff=0)
        for shape in ShapesName:
            ShapeMenu.add_command(label=shape, command=lambda text=shape: self.ChangeShape(text))
        menubar.add_cascade(label='Shapes', menu=ShapeMenu)

        ColorMenu = Menu(menubar, tearoff=0)
        ColorMenu.add_command(label='Fill Color', command=lambda mode=0: self.change_color(mode))
        ColorMenu.add_command(label='OutLine Color', command=lambda mode=1: self.change_color(mode))
        menubar.add_cascade(label='Colors', menu=ColorMenu)
        self.master.configure(menu=menubar)
        self.canvas = Canvas(self.master, width=500, height=500)
        self.canvas.pack()

    def CreateFile(self):
        if len(self.widgets) != 0:
            ans = askyesno(title='Unsaved changes', message='Do you want save content?')
            if ans:
                self.SaveFile()
        for widget in self.widgets:
            self.canvas.delete(widget)
        self.widgets.clear()

    def SaveFile(self):
        file = tkinter.filedialog.asksaveasfilename(title='Save file', filetypes=[('PostScript', '.ps')],
                                                    initialfile='NewFile.ps')
        self.canvas.postscript(file=file, colormode='color')

    def change_color(self, mode):
        temp = askcolor(title="Tkinter Color Chooser")[1]
        if temp is not None:
            if mode == 0:
                self.FillColor = temp
            else:
                self.OutLineColor = temp

    def event_handler(self, event):
        self.MouseHist.append(event)
        if self.CurShape == ShapesName.Triangle:
            if len(self.MouseHist) == 3:
                print('EventHandler: Triangle draw')
                self.widgets.append(
                    self.canvas.create_line(self.MouseHist[0].x, self.MouseHist[0].y, self.MouseHist[1].x,
                                            self.MouseHist[1].y, fill=self.FillColor, width=self.width))
                self.widgets.append(
                    self.canvas.create_line(self.MouseHist[1].x, self.MouseHist[1].y, self.MouseHist[2].x,
                                            self.MouseHist[2].y, fill=self.FillColor, width=self.width))
                self.widgets.append(
                    self.canvas.create_line(self.MouseHist[2].x, self.MouseHist[2].y, self.MouseHist[0].x,
                                            self.MouseHist[0].y, fill=self.FillColor, width=self.width))
                self.MouseHist.clear()
        elif len(self.MouseHist) == 2:
            if self.CurShape == ShapesName.Rectangle:
                self.widgets.append(
                    self.canvas.create_rectangle(self.MouseHist[0].x, self.MouseHist[0].y, self.MouseHist[1].x,
                                                 self.MouseHist[1].y, outline=self.OutLineColor,
                                                 fill=self.FillColor, width=self.width))
            elif self.CurShape == ShapesName.Ellipse:
                self.widgets.append(
                    self.canvas.create_oval(self.MouseHist[0].x, self.MouseHist[0].y, self.MouseHist[1].x,
                                            self.MouseHist[1].y, outline=self.OutLineColor, fill=self.FillColor,
                                            width=self.width))
            self.MouseHist.clear()


root = Tk()
app1 = MyFrame(root)
root.mainloop()
