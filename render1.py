from pickle import TRUE
import pygame

class Render1:
    def __init__(self, width, height, bpm):
        pygame.init()
        self.x = 100
        self.y = 100
        self.dx = 3
        self.dy = 3
        self.gameDisplay = pygame.display.set_mode((800,800))
        pygame.display.set_caption('A bit Racey')
        self.clock = pygame.time.Clock()

    def draw(self):
        BLUE =      (  0,   0, 255)
        pygame.draw.circle(self.gameDisplay, BLUE ,(self.x, self.y), 50)

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def render(self):
        while TRUE:
            self.move()
            pygame.display.update()
            self.gameDisplay.fill((0,0,0))
            self.draw()   
            self.clock.tick(60)

