import pygame
import random
import math

#circular movement
class circle:
    def __init__(self, width, height, bpm, gameDisplay):
        self.width = width
        self.height = height
        self.color = (0, 0, 0)
        self.radius = random.randint(width/20, width/10)
        self.gameDisplay = gameDisplay
        self.counter = 0
        self.radiusRoad = 100

        self.roadX = 100
        self.roadY = 100

        self.centerX = random.randint(100, 700)
        self.centerY = random.randint(100, 700)

    def draw(self):
        pygame.draw.circle(self.gameDisplay, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x = self.centerX + math.cos(math.radians(self.counter)) * (self.roadX)
        self.y = self.centerY + math.sin(math.radians(self.counter)) * (self.roadY)
        self.counter = self.counter + 1

class Render2:
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
        number = random.randint(5,10)
        for i in range(number):
            circle1 = circle(self.width, self.height, self.bpm, self.gameDisplay)
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
