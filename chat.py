import pygame

class Chat(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont('comicsans', 15)

    def draw(self, window):
        pygame.draw.rect(window, (200, 200, 200), (self.x, self.y+350, 150, 50))
        pygame.draw.rect(window, (0,0,0), (self.x, self.y, 150, 400), 5)
