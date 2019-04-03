import pygame
import sys
from Button import Button
from Button import Text

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
MENU_COLOR = (234, 255, 34)

class MenuView:
    def __init__(self, GRID_SIZE = 3, players = None):
        pygame.init()
        self.GRIDSIZE = GRID_SIZE
        self.SQUARESIZE = 300//GRID_SIZE
        self.RADIUS = int(self.SQUARESIZE/2.1)
        self.width = GRID_SIZE * self.SQUARESIZE
        self.height = (GRID_SIZE + 2) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        global Screen
        Screen = self.screen
    
    def init(self, GRID_SIZE, players):
        self.__init__(GRID_SIZE, players)

    
    def draw_Menu(self, players):
        pygame.draw.rect(self.screen, MENU_COLOR, (0, 0, self.width, self.height ))
        pygame.display.update()

        number_of_players = len(players)

        LRMargin = self.width / 20
        TDMargin = self.height / 30

        TOP = 20

        w = self.width / 2 
        h = (self.height - TOP*5) / (number_of_players+1)

        wm = w - 2 * LRMargin
        hm = h - 2 * TDMargin

        buttons1 = []
        buttons2 = []

        names_left = 27
        names_up = 8
        
        Text.headline("Player 1", names_left, names_up, 20, self.screen)
        Text.headline("Player 2", names_left+w, names_up, 20, self.screen)
        
        for i in range(number_of_players):
            x = LRMargin
            y = TOP+TDMargin+i*h
            
            B1 = Button(self.screen, x, y, w, h, wm, hm, players[i].name)
            B2 = Button(self.screen, x+w, y, w, h, wm, hm, players[i].name)

            buttons1.append(B1)
            buttons2.append(B2)

        GRID3 = Button(self.screen, x+w/2-wm*1/3, TOP+TDMargin+(number_of_players)*h, w, h, wm*2/3, hm*4/5, "3x3")
        GRID10 = Button(self.screen, x+w/2+wm*2/3, TOP+TDMargin+(number_of_players)*h, w, h, wm*2/3, hm*4/5, "10x10")

        PlayButton = Button(self.screen, x+w/2, TDMargin+(number_of_players+1)*h, w/2, h/5*4, wm, hm*5/6, "PLAY")

        pygame.display.update()

        return buttons1, buttons2, PlayButton, GRID3, GRID10

