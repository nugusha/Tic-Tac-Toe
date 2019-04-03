import pygame
import sys
from TicTacToe import TicTacToe
from Button import Button
from Button import Text
sys.path.append('./View')

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
MENU_COLOR = (234, 255, 34)

class GameView:
    def __init__(self, GRID_SIZE = 100):
        pygame.init()
        self.GRIDSIZE = GRID_SIZE
        self.SQUARESIZE = 300//GRID_SIZE
        self.RADIUS = int(self.SQUARESIZE/2.1)
        self.width = GRID_SIZE * self.SQUARESIZE
        self.height = (GRID_SIZE + 2) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
    
    def draw_game(self):
        pygame.draw.rect(self.screen, MENU_COLOR, (0, 0, self.width, self.height ))
        pygame.display.update()

        TicTacToeButton = Button(self.screen, 75, 50, 100, 100, 150, 50, "TicTacToe")
        Connect4Button = Button(self.screen, 75, 150, 100, 100, 150, 50, "Connect4")

        pygame.display.update()

        return TicTacToeButton,Connect4Button
