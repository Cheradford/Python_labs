import tkinter.filedialog
from tkinter import *
import sys, os, platform
import subprocess
import time


class MyFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, master=parent)
        self.master = parent
        self.curdir = os.getcwd()
        self.curdirs = []
        self.InitUI()

    def PrintCatalog(self):
        self.curdirs.clear()
        for i in os.listdir(self.curdir):
            temp = Button(self.master, text=i, background='white', height=1, width=30, bd=0)
            self.curdirs.append(temp)
            temp.pack()

    def CreateFile(self):
        tkinter.filedialog.asksaveasfilename()

    def OpenFile(self, msg):
        subprocess.Popen(r"notepad.exe " + msg)

    def OpenCatalog(self):
        self.curdir = tkinter.filedialog.askdirectory(initialdir=self.curdir)
        self.ReloadUI()

    def ReloadUI(self):
        for widget in self.curdirs:
            widget.pack_forget()

        self.PrintCatalog()

    def InitUI(self):
        menubar = Menu(self.master)

        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Create file", command=self.CreateFile)
        fileMenu.add_command(label="Open file", command=self.OpenFile)
        fileMenu.add_command(label="Create catalog", command=self.quit)
        fileMenu.add_command(label="Open catalog", command=self.OpenCatalog)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.master.config(menu=menubar)

        self.PrintCatalog()


root = Tk()
app1 = MyFrame(root)
root.mainloop()
