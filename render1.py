import pygame
import random

class circle:
    def __init__(self, width, height, bpm, gameDisplay):
        self.width = width
        self.height = height
        self.randomColor = (random.randint(0, 255),   random.randint(
            0, 255), random.randint(0, 255))
        self.gameDisplay = gameDisplay
        self.speedInterval = int(17189*pow(bpm, -1.7))
        self.radius = width/10
        self.x = random.randint(0+self.radius, self.width-self.radius)
        self.y = random.randint(0+self.radius, self.height-self.radius)
        self.dx = random.randint(-self.speedInterval, self.speedInterval)
        self.dy = random.randint(-self.speedInterval, self.speedInterval)
        self.acceleration = random.uniform(
            self.speedInterval*(0.003-0.001), self.speedInterval*(0.003+0.002))
        if (self.dx > 0):
            self.ddx = -self.acceleration
        else:
            self.ddx = self.acceleration

        if (self.dy > 0):
            self.ddy = -self.acceleration
        else:
            self.ddy = self.acceleration

    def draw(self):
        pygame.draw.circle(self.gameDisplay, self.randomColor,
                           (self.x, self.y), self.radius)

    def move(self):
        if ((self.dx > 0 and self.dx + self.ddx > 0) or (self.dx < 0 and self.dx + self.ddx < 0)):
            self.dx = self.dx + self.ddx
        else:
            self.dx = random.randint(-self.speedInterval, self.speedInterval)
            if (self.dx > 0):
                self.ddx = -self.acceleration
            else:
                self.ddx = self.acceleration

        if ((self.dy > 0 and self.dy + self.ddy > 0) or (self.dy < 0 and self.dy + self.ddy < 0)):
            self.dy = self.dy + self.ddy
        else:
            self.dy = random.randint(-self.speedInterval, self.speedInterval)
            if (self.dy > 0):
                self.ddy = -self.acceleration
            else:
                self.ddy = self.acceleration

        if (self.x + self.dx - self.radius < 0 or self.x + self.dx + self.radius > self.width):
            self.dx = self.dx * -1
            self.ddx = self.ddx * -1

        if (self.y + self.dy - self.radius < 0 or self.y + self.dy + self.radius > self.height):
            self.dy = self.dy * -1
            self.ddy = self.ddy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

class Render1:
    def __init__(self, width, height, bpm):
        pygame.init()
        pygame.display.set_caption('kcomtpy')
        self.width = width
        self.height = height
        self.gameDisplay = pygame.display.set_mode((width, height))
        self.bpm = bpm
        self.clock = pygame.time.Clock()
        self.gameRunning = True
        self.createBalls()

    def createBalls(self):
        self.balls = []
        number = random.randint(5, 10)
        for i in range(number):
            circle1 = circle(self.width, self.height,
                             self.bpm, self.gameDisplay)
            self.balls.append(circle1)

    def draw(self):
        for ball in self.balls:
            ball.draw()

    def move(self):
        for ball in self.balls:
            ball.move()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False

    def render(self):
        while self.gameRunning:
            self.handleEvents()
            self.move()
            pygame.display.update()
            self.gameDisplay.fill((255, 255, 255))
            self.draw()
            self.clock.tick(self.bpm)
