import cv2
import pygame
from pygame.locals import *


class PygameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Shadow Guess')

    def get_screen(self):
        return self.screen

    def display_frame(self, frame, cam_width, cam_height, cam_x, cam_y):
        # Convert OpenCV image (BGR) to Pygame image (RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pygame_frame = pygame.image.frombuffer(frame.flatten(), (cam_width, cam_height), 'RGB')

        # Display the Pygame image
        self.screen.blit(pygame_frame, (cam_x, cam_y))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                cv2.destroyAllWindows()
