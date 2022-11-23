import sys
import array


def print_menu():
    print("1 - Divine by zero")
    print("2 - Index exception")
    print("3 - Name exception")
    print("4 - File not found")
    print("5 - Type error")
    print("6 - Выход")


def disp(msg):
    if msg == "1": ZeroException()
    if msg == "2": IndexException()
    if msg == "3": NameException()
    if msg == "4": FileException()
    if msg == "5": TypeException()
    if msg == "6" or msg == "q": sys.exit(0)


def ZeroException():
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print(ZeroDivisionError)


def IndexException():
    try:
        arr = array.array('i', [10, 20, 30])
        print(arr[5])
    except IndexError:
        print(IndexError)


def NameException():
    try:
        print(f)
    except NameError:
        print(NameError)


def FileException():
    try:
        file = open("file.txt","r")
    except FileNotFoundError:
        print(FileNotFoundError)




def TypeException():
    try:
        i = 1
        str = "hello world!"
        print(str + i)
    except TypeError:
        print(TypeError)


def main_loop():
    while True:
        print_menu()
        msg = input("#>")
        disp(msg)


main_loop()
