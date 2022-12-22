import random
from tkinter import *



class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
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

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.map = [[]]
        self.way = []
        length = 49
        self.exit = Coordinates(random.randint(0, length), random.randint(0, length))
        self.player = Car(Coordinates(random.randint(0, length), random.randint(0, length)))

        print('player:', self.player.loc.x, ' ', self.player.loc.y)
        print('exit:' , self.exit.x, ' ', self.exit.y)
        for i in range(0, length + 1):
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
        self.way.append(Coordinates(self.player.getLoc().x, self.player.getLoc().y))
        self.Move()
        self.way.append(self.exit)

        self.initUI()

    def Move(self):
        while self.player.loc != self.exit:
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
            self.way.append(Coordinates(player.x, player.y))


    def initUI(self):
        scale = 10
        self.master.title("The way")
        self.pack(fill=BOTH, expand=1)
        self.config(width=50 * scale, height=50 * scale)

        canvas = Canvas(self)
        canvas.pack()

        for i in range(0,6):
            point1 = self.way[i]
            canvas.create_oval(point1.x * scale, point1.y * scale, point1.x * scale, point1.y * scale, fill='red', width=scale)

        for i in range(7, len(self.way)):
            point1 = self.way[i - 1]
            point2 = self.way[i]
            print(i - 1, ':\t', point1.x, ' ', point1.y)
            print(i, ':\t', point2.x, ' ', point2.y)
            canvas.create_line(point1.x * scale, point1.y * scale, point2.x * scale, point2.y * scale, fill='green', width=scale)

        canvas.pack(fill=BOTH, expand=1)


root = Tk()
root.geometry('500x500')
ex = Example(root)
root.mainloop()
