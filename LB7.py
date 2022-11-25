from tkinter import *
import sys,os,platform
import subprocess
import time

class MyFrame(Frame):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.curdir = os.getcwd()
        self.curdirs = []
        self.InitUI()

    def CreateFile(self):
        TempWind = Toplevel(self.parent)
        TempWind.title('Create file')

    def InitUI(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Create file", command=self.CreateFile())
        fileMenu.add_command(label="Create catalog", command=self.quit())
        fileMenu.add_command(label="Exit", command=self.quit())
        menubar.add_cascade(label="File", menu=fileMenu)


root = Tk()
app = MyFrame(root)
root.mainloop()