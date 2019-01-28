from os import system
import numpy as np
import random

class HumanPlayer():
    def __init__(self):
        pass
    def make_a_move(self,board,pygame,SQUARESIZE):
        GRID_SIZE = len(board[0])
        while (True):
            for event in pygame.event.get():
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = posx // SQUARESIZE
                    row = posy // SQUARESIZE - 1
                    next = row * GRID_SIZE + col
                    return next
        return -1
