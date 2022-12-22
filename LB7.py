import tkinter.filedialog
from tkinter import *
import os
import subprocess
import time


class MyFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, master=parent)
        self.master = parent
        self.curdir = os.path.curdir
        self.curdirs = []
        self.InitUI()
        self.stats = ['Режим файла', 'Индекс файла', 'Идентификатор устройства', 'Количество жестких ссылок',
                      'Идентификатор пользователя владельца файла', 'Групповой идентификатор владельца файла',
                      'Размер файла в байтах', 'Время последнего доступа', 'Время последней модификации контента']

    def EventListener(self, text):
        if os.path.isdir(os.getcwd() + '\\' + text):
            os.chdir(text)
            self.curdir = os.path.curdir
        else:
            self.curdir = os.path.curdir + '\\' + text

        self.ReloadUI()

    def CreateExitButton(self):
        exitButton = Button(self.master, text='..', background='white', height=1, width=30, bd=0,
                            command=lambda text='..': self.EventListener(text))
        self.curdirs.append(exitButton)
        exitButton.pack()

    def PrintCatalog(self):
        self.CreateExitButton()
        for i in os.listdir(self.curdir):
            temp = Button(self.master, text=i, background='white', height=1, width=30, bd=0,
                          command=lambda text=i: self.EventListener(text))
            self.curdirs.append(temp)
            temp.pack()

    def PrintStat(self):
        stats = os.stat(self.curdir)
        index = 0
        self.CreateExitButton()
        for text in self.stats:
            if index < 7:
                temp = Label(text=text + ': ' + str(stats[index]))
            else:
                temp = Label(text=text + ': ' + time.strftime("%d.%m.%Y", time.localtime(stats[index])))
            index += 1
            temp.pack()
            self.curdirs.append(temp)

    def PrintDialog(self):
        T = Text(self.master)
        T.pack()
        self.curdirs.append(T)
        Saver = Button(self.master, text='Сохранить', background='white', height=1, width=30, bd=0,
                       command=lambda filename=os.path.abspath(self.curdir): self.SaveContent(filename))
        Saver.pack()
        self.curdirs.append(Saver)

    def CreateCatalog(self):
        self.curdir = tkinter.filedialog.askdirectory(initialdir=self.curdir)
        path = os.path.join(self.curdir, 'NewDirectory')
        os.makedirs(path)
        self.ReloadUI()

    def CreateFile(self):
        self.curdir = tkinter.filedialog.asksaveasfilename()
        print(self.curdir)
        self.ReloadUI()

    def OpenFile(self, msg):
        print(msg + self.curdir)
        subprocess.Popen(r"notepad.exe " + msg + self.curdir)

    def OpenCatalog(self):
        self.curdir = tkinter.filedialog.askdirectory(initialdir=self.curdir)
        self.ReloadUI()

    def SaveContent(self, filename):
        print(self.curdirs)
        file = open(filename, 'w+')
        file.write(self.curdirs[0].get('1.0', END))
        file.close()
        self.EventListener('..')

    def ReloadUI(self):
        for widget in self.curdirs:
            widget.pack_forget()
        self.curdirs.clear()

        if os.path.isdir(self.curdir):
            self.PrintCatalog()
        else:
            if os.path.exists(self.curdir):
                self.PrintStat()
            else:
                self.PrintDialog()

    def InitUI(self):
        menubar = Menu(self.master)

        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Create file", command=self.CreateFile)
        fileMenu.add_command(label="Open file", command=lambda text=os.path.abspath(self.curdir): self.OpenFile(text))
        fileMenu.add_command(label="Create catalog", command=self.CreateCatalog)
        fileMenu.add_command(label="Open catalog", command=self.OpenCatalog)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.master.config(menu=menubar)

        self.PrintCatalog()


root = Tk()
app1 = MyFrame(root)
root.mainloop()
