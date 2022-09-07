import pygame
import random

class circle:
    def __init__(self, width, height, gameDisplay, radius, colorBlack):
        self.width = width
        self.height = height
        self.gameDisplay = gameDisplay
        self.radius = radius
        self.x = 0
        self.y = 0

        print("x ", self.x)
        print("y ", self.y)
        if (colorBlack):
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)

    def draw(self):
        pygame.draw.circle(self.gameDisplay, self.color,
                           (self.x, self.y), self.radius)

class Render4:
    def __init__(self, width, height, bpm):
        pygame.init()
        pygame.display.set_caption('kcomtpy')
        self.width = width
        self.height = height
        self.gameDisplay = pygame.display.set_mode((width, height))
        self.bpm = bpm
        self.clock = pygame.time.Clock()
        self.gameRunning = True
        self.radius = self.width
        self.balls = []
        self.colorBlack = True

    def createBall(self):
        circle1 = circle(self.width, self.height,
                         self.gameDisplay, self.radius, self.colorBlack)
        self.radius = self.radius - 10
        self.colorBlack = not self.colorBlack
        self.balls.append(circle1)

    def draw(self):
        self.createBall()
        for ball in self.balls:
            ball.draw()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False

    def render(self):
        while self.gameRunning:
            self.handleEvents()
            pygame.display.update()
            self.gameDisplay.fill((0, 0, 0))
            self.draw()
            self.clock.tick(self.bpm/2)
