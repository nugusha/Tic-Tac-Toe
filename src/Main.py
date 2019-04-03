"""
main py file to run the game
"""
import sys
import pygame
sys.path.append('./Controller')
sys.path.append('./Model')
sys.path.append('./View')
from MainController import MainController
from GameController import GameController
from GameView import GameView
from MenuView import MenuView

if __name__ == '__main__':

    GameController(GameView())

    MainController(MenuView()).run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
