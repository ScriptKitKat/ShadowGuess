import pygame
import cv2
from leaderboard import Leaderboard
from top_section import TopSection
from Camera import Camera
from pyWindow import PygameWindow
from chat import Chat

class Game(object):
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.window = PygameWindow(self.width, self.height)
        self.chat = Chat(1000, 150)
        self.leaderboard = Leaderboard(15, 150)
        self.camera = Camera(310, 120, self.window)
        self.top_section = TopSection(10, 10, 1000, 100)


    def draw(self):
        self.window.get_screen().fill((255, 255, 255))
        self.leaderboard.draw(self.window.get_screen())
        self.top_section.draw(self.window.get_screen())
        self.chat.draw(self.window.get_screen())
        self.camera.feed()
        pygame.display.update()

    def run(self):
        run = True
        pygame.init()
        pygame.display.init()
        while run:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    cv2.destroyAllWindows()
                    break

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
