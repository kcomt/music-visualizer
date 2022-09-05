import pygame
import random

class circle:
    def __init__(self, width, height, bpm, gameDisplay, order):
        self.width = width
        self.height = height
        self.randomColor = (255,255,255)
        self.gameDisplay = gameDisplay
        self.radius = width/15

        if(order == 1):
            self.x = self.radius*2
            self.y = self.radius*2
            self.dx = bpm/4
            self.dy = bpm*2

        elif (order == 2):
            self.x = width-self.radius*2
            self.y = self.radius*2
            self.dx = bpm/4
            self.dy = bpm*2

        elif (order == 3):
            self.x = self.radius*2
            self.y = self.radius*2
            self.dx = bpm*2
            self.dy = bpm/4

        elif (order == 4):
            self.x = self.radius*2
            self.y = height-self.radius*2
            self.dx = bpm*2
            self.dy = bpm/4


    def draw(self):
        pygame.draw.circle(self.gameDisplay, self.randomColor, (self.x, self.y), self.radius)

    def move(self):
        if (self.x + self.dx - self.radius < 0 or self.x + self.dx + self.radius > self.width):
            self.dx = self.dx * -1
        
        if (self.y + self.dy - self.radius< 0 or self.y + self.dy + self.radius> self.height):
            self.dy = self.dy * -1
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy

class rectangle:
    def __init__(self, width, height, bpm, gameDisplay, order):
        self.width = width
        self.height = height
        self.randomColor = (255,255,255)
        self.gameDisplay = gameDisplay
        self.radius = width/15

        if(order == 1):
            self.x = self.radius*2
            self.y = self.radius*2
            self.dx = bpm/4
            self.dy = bpm*2

        elif (order == 2):
            self.x = width-self.radius*2
            self.y = self.radius*2
            self.dx = bpm/4
            self.dy = bpm*2

        elif (order == 3):
            self.x = self.radius*2
            self.y = self.radius*2
            self.dx = bpm*2
            self.dy = bpm/4

        elif (order == 4):
            self.x = self.radius*2
            self.y = height-self.radius*2
            self.dx = bpm*2
            self.dy = bpm/4


    def draw(self):
        #pygame.draw.circle(self.gameDisplay, self.randomColor, (self.x, self.y), self.radius)
        pygame.draw.rect(self.gameDisplay, self.randomColor, (self.x, self.y, self.radius, self.radius))

    def move(self):
        if (self.x + self.dx - self.radius < 0 or self.x + self.dx + self.radius > self.width):
            self.dx = self.dx * -1
        
        if (self.y + self.dy - self.radius< 0 or self.y + self.dy + self.radius> self.height):
            self.dy = self.dy * -1
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy

class Render3:
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
        circle1 = rectangle(self.width, self.height, self.bpm, self.gameDisplay, 1)
        circle2 = rectangle(self.width, self.height, self.bpm, self.gameDisplay, 2)
        circle3 = circle(self.width, self.height, self.bpm, self.gameDisplay, 3)
        circle4 = circle(self.width, self.height, self.bpm, self.gameDisplay, 4)
        self.balls.append(circle1)
        self.balls.append(circle2)
        self.balls.append(circle3)
        self.balls.append(circle4) 

    def draw(self):
        for ball in self.balls:
            ball.draw()

        font = pygame.font.SysFont('Arial', 15, True)
        text1 = font.render('Position x: ' + str(self.balls[0].x)[0:5], False, (255, 255, 255))
        text2 = font.render('Position y: ' + str(self.balls[0].y)[0:5], False, (255, 255, 255))

        self.gameDisplay.blit(text1,(5, 5))
        self.gameDisplay.blit(text2,(5, 24))

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
            self.gameDisplay.fill((0, 0, 0))
            self.draw()
            self.clock.tick(self.bpm/2)
