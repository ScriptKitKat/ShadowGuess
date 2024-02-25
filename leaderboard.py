import pygame
pygame.init()
class Leaderboard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 80
        self.font = pygame.font.SysFont('comicsans', 20)

    def draw(self, window):
        players = [("Bob", 300),("Tom", 200),("Jerry", 100)]

        for i, player in enumerate(players):

            pygame.draw.rect(window, (0,0,0), (self.x, self.y + i*self.height, self.width, self.height), 5)

            # names
            place = self.font.render("#" + str(i + 1), 1, (0,0,0))
            window.blit(place, (self.x + 10, self.y + i*self.height + 20))

            name = self.font.render(str(player[0]), 1, (0, 0, 0))
            window.blit(name, (self.x + 50, self.y + i*self.height + 20))

            score = self.font.render(str(player[1]), 1, (0, 0, 0))
            window.blit(score, (self.x + 130, self.y + i*self.height + 20))