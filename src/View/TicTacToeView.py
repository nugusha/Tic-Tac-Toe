import pygame
import sys
from Button import Button
from Button import Text

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class TicTacToeView:
    def __init__(self,GRID_SIZE):
        pygame.init()
        self.SQUARESIZE = 300//GRID_SIZE
        self.RADIUS = int(self.SQUARESIZE/2.1)
        self.width = GRID_SIZE * self.SQUARESIZE
        self.height = (GRID_SIZE + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.myfont = pygame.font.SysFont("monospace", self.SQUARESIZE//3)
        self.BackButton = None
    
    def draw_board(self,board):
        GRIDSIZE = len(board[0])
        SQUARESIZE = self.SQUARESIZE
        RADIUS = self.RADIUS
        
        self.BackButton = Button(self.screen, self.width-80, 0, 80, 50, 75, 45, "Back")
        self.BackButton.draw_button(YELLOW)
        print("!!")
        for c in range(GRIDSIZE):
            for r in range(GRIDSIZE):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE,(r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE ))
                if( board[r][c] == 1):
                    color = YELLOW
                if( board[r][c] == -1):
                    color = RED
                if( board[r][c] == 0):
                    color = WHITE
                pygame.draw.circle(self.screen, color, (int(c*SQUARESIZE+SQUARESIZE/2),int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def draw_turn(self,name):
        pygame.draw.rect(self.screen, BLACK, (0,0,self.width,self.SQUARESIZE))
        self.headline(name)
        self.BackButton.draw_button(YELLOW)
        pygame.display.update()
    
    def gameover(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
    
    def WAIT(self,duration):
        pygame.time.wait(duration)
    
    def WaitForAClick(self):
        while(True):
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.BackButton.isClicked(event)):
                        return 1000
                    return 0
                if (event.type == pygame.QUIT):
                    sys.exit()
                    
    def isBackButtonClicked(self):
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(self.BackButton.isClicked(event)):
                    return True
        return False
    
    def headline(self,headline):
        pygame.draw.rect(self.screen, BLACK, (0,0,self.width,self.SQUARESIZE))
        self.BackButton.draw_button(YELLOW)
        print(headline)
        label = self.myfont.render(headline, 1 , YELLOW)
        self.screen.blit(label, (25, 10))
        pygame.display.update()
    
    def getPYGAME(self):
        return pygame