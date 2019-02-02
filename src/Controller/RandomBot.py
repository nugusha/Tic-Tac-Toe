import random

class RandomBot():
    def __init__(self,name = 'Bot'):
        self.name = name
    def make_a_move(self,board):
        GRID_SIZE = len(board[0])
        x = random.randint(0,GRID_SIZE**2-1)
        while(board[x//GRID_SIZE][x%GRID_SIZE]!=0):
            x = random.randint(0,GRID_SIZE**2-1)
        return x
