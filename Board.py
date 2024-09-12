import pygame
import sys
import numpy as np
from keras.models import load_model
import cv2

# Constants
WINDOWSIZEX = 640
WINDOWSIZEY = 480
BOUNDRYINC = 5
PREDICT = True
IMAGESAVE = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load the model
MODEL = load_model("bestmodel.keras")

# Define labels
LABELS = {0: "Zero", 1: "One",
          2: "Two", 3: "Three",
          4: "Four", 5: "Five",
          6: "Six", 7: "Seven",
          8: "Eight", 9: "Nine", 
          'A': "A", 'B': "B", 'C': "C", 'D': "D", 'E': "E",
          'F': "F", 'G': "G", 'H': "H", 'I': "I", 'J': "J",
          'K': "K", 'L': "L", 'M': "M", 'N': "N", 'O': "O",
          'P': "P", 'Q': "Q", 'R': "R", 'S': "S", 'T': "T",
          'U': "U", 'V': "V", 'W': "W", 'X': "X", 'Y': "Y",
          'Z': "Z"}

# Initialize pygame
pygame.init()
displaysurf = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
pygame.display.set_caption("Digit_Board")
iswriting = False

# Define font
FONT = pygame.font.Font(None, 36)  # Default font and size

number_xcord = []
number_ycord = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION and iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(displaysurf, WHITE, (xcord, ycord), 4, 0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)

        if event.type == pygame.MOUSEBUTTONDOWN:
            iswriting = True

        if event.type == pygame.MOUSEBUTTONUP:
            iswriting = False
            
            # Check if the lists are not empty
            if number_xcord and number_ycord:
                number_xcord = sorted(number_xcord)
                number_ycord = sorted(number_ycord)
                
                rect_min_x = max(number_xcord[0] - BOUNDRYINC, 0)
                rect_max_x = min(number_xcord[-1] + BOUNDRYINC, WINDOWSIZEX)
                rect_min_y = max(number_ycord[0] - BOUNDRYINC, 0)
                rect_max_y = min(number_ycord[-1] + BOUNDRYINC, WINDOWSIZEY)
                
                number_xcord = []
                number_ycord = []

                # Extract the image array
                img_arr = np.array(pygame.PixelArray(displaysurf))[rect_min_x:rect_max_x, rect_min_y:rect_max_y].T.astype(np.float32)

                if IMAGESAVE:
                    cv2.imwrite("image.png", img_arr)

                if PREDICT:
                    image = cv2.resize(img_arr, (28, 28))
                    image = np.pad(image, (10, 10), 'constant', constant_values=0)
                    image = cv2.resize(image, (28, 28)) / 255
                    label = str(LABELS[np.argmax(MODEL.predict(image.reshape(1, 28, 28, 1)))])
                    
                    textSurface = FONT.render(label, True, RED, WHITE)
                    textRectObj = textSurface.get_rect()
                    textRectObj.left, textRectObj.bottom = rect_min_x, rect_max_y
                    displaysurf.blit(textSurface, textRectObj)

        if event.type == pygame.KEYDOWN:
            if event.unicode == "n":
                displaysurf.fill(BLACK)

        pygame.display.update()
