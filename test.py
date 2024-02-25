import cv2
import pygame
from pygame.locals import *
import mediapipe as mp

class PygameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Pygame Window')

    def get_screen(self):
        return self.screen

    def display_frame(self, frame):
        # Convert OpenCV image (BGR) to Pygame image (RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pygame_frame = pygame.image.frombuffer(frame.flatten(), (self.width, self.height), 'RGB')

        # Display the Pygame image
        self.screen.blit(pygame_frame, (0, 0))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                cv2.destroyAllWindows()


class OpenCVIntegration:
    def __init__(self, pygame_window):
        self.pygame_window = pygame_window
        self.cap = cv2.VideoCapture(0)
        self.mp_drawing = mp.solutions.drawing_utils
        mp_hand = mp.solutions.hands
        self.mp_hand = mp.solutions.hands
        self.hand = mp_hand.Hands()

    def run(self):
        while True:
            ret, frame = self.cap.read()
            # RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # result = self.hand.process(RGB_frame)
            #
            # if result.multi_hand_landmarks:
            #     for hand_landmarks in result.multi_hand_landmarks:
            #         self.mp_drawing.draw_landmarks(frame, hand_landmarks, connections=self.mp_hand.HAND_CONNECTIONS)
            if not ret:
                break

            # Process the frame or perform other OpenCV operations as needed

            # Display the frame in the Pygame window
            self.pygame_window.display_frame(frame)

            # Handle Pygame events
            self.pygame_window.handle_events()


if __name__ == "__main__":
    pygame.init()

    # Set the dimensions of the Pygame window
    window_width, window_height = 640, 480

    # Create an instance of the PygameWindow class
    pygame_window = PygameWindow(window_width, window_height)

    # Create an instance of the OpenCVIntegration class and pass the PygameWindow instance
    opencv_integration = OpenCVIntegration(pygame_window)

    # Run the integration
    opencv_integration.run()
