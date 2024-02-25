import pygame
pygame.init()
class TopSection(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.story = "Cinderella"
        self.font = pygame.font.SysFont("comicsans", 50)
        self.round = 1

    def draw(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x, self.y, self.width, self.height), 7)
        round = self.font.render("Round 1 of 2", 1, (0,0,0))
        window.blit(round, (self.x + 10, self.y + 20))

        underscores = self.font.render("_ _ _ _ _ _ _ _", 1, (0, 0, 0))
        window.blit(underscores, (self.x + 450, self.y + 20))