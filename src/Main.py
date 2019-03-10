import sys
import pygame
sys.path.append('./Controller')
sys.path.append('./View')
from MainController import *
from GameController import *

if __name__ == '__main__':

    GAME = GameController()

    MENU = MainController()
    RESULT = MENU.run()
    print(RESULT)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
