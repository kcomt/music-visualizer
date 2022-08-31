from pickle import TRUE
from turtle import width
import pygame
import random


class Render1:
    def __init__(self, width, height, bpm):
        pygame.init()
        self.width = width
        self.height = height
        self.gameDisplay = pygame.display.set_mode((width, height))
        self.bpm = bpm
        self.x = 100
        self.y = 100
        self.radius = width/10
        self.dx = 2
        self.dy = 3
        pygame.display.set_caption('kcomtpy')
        self.clock = pygame.time.Clock()
        self.gameRunning = TRUE
        self.randomColor = (random.randint(0, 255),   random.randint(
            0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(self.gameDisplay, self.randomColor, (self.x, self.y), self.radius)

    def move(self):
        moveX = random.randint(0, 100)
        moveY = random.randint(0, 100)
        
        if (moveX == 99):
            self.dx = self.dx * -1
            
        if (moveY == 99):
            self.dy = self.dy * -1

        if (self.x + self.dx - self.radius < 0 or self.x + self.dx + self.radius > self.width):
            self.dx = self.dx * -1
        
        if (self.y + self.dy - self.radius< 0 or self.y + self.dy + self.radius> self.height):
            self.dy = self.dy * -1
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy

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
