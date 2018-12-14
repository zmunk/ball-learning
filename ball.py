import pygame as pg
from threading import Thread

black = (0, 0, 0)
white = (255, 255, 255)


class Screen:
    width = 800
    height = 600
    def __init__(self):
        self.bgColor = white

        pg.init()
        self.display = pg.display.set_mode((Screen.width, Screen.height))
        self.display.fill(self.bgColor)
        self.clock = pg.time.Clock()

        self.objects = []

        Thread(target=self.update).start()

    def update(self):
        while True:
            self.checkStatus()
            self.display.fill(self.bgColor)
            for obj in self.objects:
                obj.draw()
            pg.display.update()
            self.clock.tick(60)

    def checkStatus(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def addObject(self, obj):
        self.objects.append(obj)


class Ball:
    def __init__(self, screen, x, y, r=10):
        self.display = screen.display
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.r = r
        self.color = black

        screen.addObject(self)

    def draw(self):
        if self.x >= Screen.width:
            self.vx = -abs(self.vx)
        if self.x <= 0:
            self.vx = abs(self.vx)
        if self.y >= Screen.height:
            self.vy = -abs(self.vy)
        if self.y <= 0:
            self.vy = abs(self.vy)
        self.x += self.vx
        self.y += self.vy
        pg.draw.circle(self.display, black, (self.x, self.y), self.r)

    def updateVelocity(self, vx, vy):
        self.vx = vx
        self.vy = vy


if __name__ == '__main__':
    screen = Screen()
    ball = Ball(screen, 400, 300)
    ball.updateVelocity(3, 1)
    ball2 = Ball(screen, 100, 400)
    ball2.updateVelocity(5, -2)

