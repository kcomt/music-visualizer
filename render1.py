from pickle import TRUE
from turtle import width
import pygame
import random


class Render1:
    def __init__(self, width, height, bpm):
        pygame.init()
        pygame.display.set_caption('kcomtpy')

        self.width = width
        self.height = height
        self.gameDisplay = pygame.display.set_mode((width, height))
        self.bpm = bpm
        self.x = 100
        self.y = 100
        self.radius = width/20
        self.clock = pygame.time.Clock()
        self.gameRunning = TRUE
        self.randomColor = (random.randint(0, 255),   random.randint(
            0, 255), random.randint(0, 255))

        self.speedInterval = 10
        self.acceleration = self.speedInterval*0.03
        self.dx = random.randint(-self.speedInterval, self.speedInterval)
        self.dy = random.randint(-self.speedInterval, self.speedInterval)

        if(self.dx > 0):
            self.ddx = -self.acceleration
        else:
            self.ddx = self.acceleration
        
        if(self.dy > 0):
            self.ddy = -self.acceleration
        else:
            self.ddy = self.acceleration

    def draw(self):
        pygame.draw.circle(self.gameDisplay, self.randomColor, (self.x, self.y), self.radius)

    def move(self):

        if((self.dx > 0 and self.dx + self.ddx > 0) or (self.dx < 0 and self.dx + self.ddx < 0)):
            self.dx = self.dx + self.ddx
        else:
            self.dx = random.randint(-self.speedInterval, self.speedInterval)
            if(self.dx > 0):
                self.ddx = -self.acceleration
            else:
                self.ddx = self.acceleration

        if((self.dy > 0 and self.dy + self.ddy > 0) or (self.dy < 0 and self.dy + self.ddy < 0)):
            self.dy = self.dy + self.ddy
        else:
            self.dy = random.randint(-self.speedInterval, self.speedInterval)
            if(self.dy > 0):
                self.ddy = -self.acceleration
            else:
                self.ddy = self.acceleration

        if (self.x + self.dx - self.radius < 0 or self.x + self.dx + self.radius > self.width):
            self.dx = self.dx * -1
            self.ddx = self.ddx * -1
        
        if (self.y + self.dy - self.radius< 0 or self.y + self.dy + self.radius> self.height):
            self.dy = self.dy * -1
            self.ddy = self.ddy * -1
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        print("dx",self.dx)
        print("ddx",self.ddx)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False

    def render(self):
        while self.gameRunning:
            self.handleEvents()
            self.move()
            pygame.display.update()
            self.gameDisplay.fill((0, 0, 0))
            self.draw()
            self.clock.tick(self.bpm)
