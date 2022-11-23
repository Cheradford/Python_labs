import random
import copy
from tkinter import *
from tkinter import ttk


class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Coordinates(self, x: int, y: int):
        self.__init__()
        self.x = x
        self.y = y


class Car:

    def __init__(self, loc):
        self.loc = loc

    def Car(self, loc: Coordinates):
        self.loc = loc

    def getLoc(self):
        return self.loc

    def toMove(self, x, y):
        while self.loc.x != x and self.loc.y != y:
            if self.loc.x < x: self.loc.x += 1
            if self.loc.x > x: self.loc.x -= 1
            if self.loc.y < y: self.loc.y += 1
            if self.loc.y > y: self.loc.y -= 1


class Example(Frame):

    def Compare(self, x1, x2):
        if x1 < x2: return -1
        if x1 == x2: return 0
        if x1 > x2: return 1

    def __init__(self):
        super().__init__()
        self.map = [[]]
        self.way = []
        length = 50
        self.exit = Coordinates(random.randint(0, length), random.randint(0, length))
        self.player = Car(Coordinates(random.randint(0, length), random.randint(0, 50)))
        self.way.append(Coordinates(self.player.getLoc().x, self.player.getLoc().y))

        for i in range(0, length):
            self.map.append([])
            for j in range(0, length):
                self.map[i].append(True)

        for i in range(0, 5):
            x = random.randint(0, length)
            y = random.randint(0, length)
            temp = Coordinates(x, y)
            while temp == self.player.loc or temp == self.exit:
                x = random.randint(0, length)
                y = random.randint(0, length)
                temp = Coordinates(x, y)
            self.way.append(temp)
            self.map[x][y] = False

        self.Move()
        self.way.append(self.exit)

        self.initUI()

    def Move(self):
        while self.player != self.exit:
            player = self.player.loc
            dx = self.Compare(self.exit.x, player.x)
            dy = self.Compare(self.exit.y, player.y)

            if self.map[player.x + dx][player.y + dy]:
                player.x += dx
                player.y += dy
            elif (((self.exit.x - player.x) * dx) > ((self.exit.y - player.y) * dy)) and (self.map[player.x + dx][player.y]):
                player.x += dx
            elif self.map[player.x][player.y + dy]:
                player.y +=dy
            elif self.map[player.x - dy][player.y + dy]:
                player.x -= dy
                player.y += dy
            elif self.map[player.x + dy][player.y + dy]:
                player.x += dy
                player.y += dy
            else: break
            self.player.toMove(player.x, player.y)
            self.way.append(copy.copy(player))


    def initUI(self):
        self.master.title("The way")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack()
        for i in range(1, len(self.way)):
            point1 = self.way[i - 1]
            point2 = self.way[i]
            canvas.create_line(point1.x, point1.y, point2.x, point2.y, fill='green', width=10)

        canvas.pack(fill=BOTH, expand=1)


root = Tk()
ex = Example()
root.mainloop()
