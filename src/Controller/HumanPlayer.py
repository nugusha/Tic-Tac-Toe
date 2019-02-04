import sys
import pygame

class HumanPlayer():
    def __init__(self,x = 1,name = 'Human'):
        self.name = name
        self.x = x
    def make_a_move(self,board):
        GRID_SIZE = len(board[0])
        width = pygame.display.get_surface().get_size()[0]
        SQUARESIZE = width // GRID_SIZE
        while (True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = posx // SQUARESIZE
                    row = posy // SQUARESIZE - 1
                    next = row * GRID_SIZE + col
                    return next
        return -1