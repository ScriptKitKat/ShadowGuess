import cv2

class Camera(object):
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.width = 640
        self.height = 480
        self.cap = cv2.VideoCapture(0)
        self.pygame_window = window

    def feed(self):
        while True:
            success, frame = self.cap.read()

            blur = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(blur, (5, 5), 0)

            thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            thresh = cv2.erode(thresh, None, iterations=2)
            thresh = cv2.dilate(thresh, None, iterations=2)

            # contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]
            # TODO: Find a way to track contours so only the hand is display

            if not success:
                break

            self.pygame_window.display_frame(thresh, self.width, self.height, self.x, self.y)

            # Handle Pygame events
            self.pygame_window.handle_events()

