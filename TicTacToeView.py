
import pygame

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class TicTacToeView:
    def __init__(self,size,SQUARESIZE):
        pygame.init()
        self.SQUARESIZE = SQUARESIZE
        self.width = size[0]
        self.height = size[1]
        self.screen = pygame.display.set_mode(size)
        self.myfont = pygame.font.SysFont("monospace", SQUARESIZE//2)
    
    def draw_board(self,board,GRIDSIZE,SQUARESIZE,RADIUS):
        print(board,GRIDSIZE)
        for c in range(GRIDSIZE):
            for r in range(GRIDSIZE):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE,(r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE ))
                if( board[r][c] == 'X'):
                    color = YELLOW
                if( board[r][c] == 'O'):
                    color = RED
                if( board[r][c] == '.'):
                    color = WHITE
                pygame.draw.circle(self.screen, color, (int(c*SQUARESIZE+SQUARESIZE/2),int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                pygame.display.update()

    def draw_turn(self,turn,human):
        pygame.draw.rect(self.screen, BLACK, (0,0,self.width,self.SQUARESIZE))
        if(turn == human):
            self.headline("Your Turn!")
        else:
            self.headline("Bot Turn!")
        pygame.display.update()
                
    
    def headline(self,headline):
        pygame.draw.rect(self.screen, BLACK, (0,0,self.width,self.SQUARESIZE))
        print(headline)
        label = self.myfont.render(headline, 1 , YELLOW)
        self.screen.blit(label, (25, 10))
        pygame.display.update()