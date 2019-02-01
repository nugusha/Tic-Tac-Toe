from os import system
import numpy as np
import random

class RandomBot():
    def __init__(self,name = 'Bot'):
        self.name = name
    def make_a_move(self,board,pygame=0):
        GRID_SIZE = len(board[0])
        x = random.randint(0,GRID_SIZE**2-1)
        while(board[x//GRID_SIZE][x%GRID_SIZE]!=0):
            x = random.randint(0,GRID_SIZE**2-1)
        return x
