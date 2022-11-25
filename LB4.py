# -*- coding: utf-8 -*-

import sys,os,platform
import subprocess
import time

hlp = """Программа - файловый эксплорер"""

ar = sys.argv
curdir = os.getcwd()
curdirs = []

if (len(ar) > 1) and (ar[1] == "-h"):
    print(hlp)
    sys.exit(0)

def print_main_menu():
    print("ls\t- содержание каталога")
    print("prp\t- копировать файл")
    print("opn\t- открыть файл")
    print("crt\t- создать файл или каталог")
    print("del\t- удалить файл")
    print("up\t- выйти из текущего каталога")
    print("dwn\t- войти в каталог")
    print("q\t- выход")
    print("\n")

def list_dir():
    global curdir, curdirs
    lst = []
    item = ""
    for item in os.listdir(curdir):
        if os.path.isdir(item):
            curdirs.append(item)
            item = "[" + item + "]"

        lst.append(item)
    lst.reverse()

    for item in lst: print(item)


def property_file(msg):
    global curdir
    path = curdir + "\\" + msg
    if not os.path.exists(r"" + path): return
    prp = os.stat(r""+ path)
    print("Размер файла\t- "+ str(prp.st_size))
    print("Последнее открытие\t- " + time.strftime("%d.%m.%Y %S:%M:H", time.localtime(prp.st_atime)))
    print("Создание файла\t- " + time.strftime("%d.%m.%Y %S:%M:H", time.localtime(prp.st_ctime)))
    print("Изменение файла\t- " + time.strftime("%d.%m.%Y %S:%M:H", time.localtime(prp.st_mtime)))



def open_file(msg):
    subprocess.Popen(r"notepad.exe " + msg)

def create_file(msg) :
    global curdir

    path = curdir + "\\" + msg[0]
    if len(msg) == 1:
        os.mkdir(path)
    if len(msg) == 2:
        if not os.path.exists(r"" + path):
            file = open(path, 'w')
            if len(msg) == 2:
                file.write(msg[1])
        else:
            print("Файл с таким именем уже существует")


def delete_file(msg) :
    global curdir
    path = curdir + '\\' + msg
    if platform.system() == 'Windows': os.remove(path)
    else: os.unlink(path)


def up_dir():
    global  curdir
    curdir = os.chdir('..')

def down_dir(msg):
    global curdir
    curdir = os.chdir(os.curdir +'\\'+msg)

def validate(msg):
    lst1 = ["ls", "up", "q"]
    lst2 = ["prp", "dwn", "q", "opn", 'del']
    lst3 = ['crt']

    if msg == "": return False

    if lst1.count(msg[0]) and len(msg) == 1: return True
    if lst2.count(msg[0]) and len(msg) == 2: return True
    if lst3.count(msg[0]) and (len(msg) == 3 or len(msg) == 2): return True

    return False


def disp(msg):
    msg = msg.split(' ')
    if not validate(msg): return
    if msg[0] == "q": exit(0)
    if msg[0] == "ls" : list_dir()
    if msg[0] == "prp" : property_file(msg[1])
    if msg[0] == "opn" : open_file(msg[1])
    if msg[0] == "crt" : create_file(msg[1:])
    if msg[0] == "del" : delete_file(msg[1])
    if msg[0] == "up" : up_dir()
    if msg[0] == "dwn" : down_dir(msg[1])


def main_loop():
    while(True):
        print_main_menu()
        msg = input("#>")
        disp(msg)

main_loop()