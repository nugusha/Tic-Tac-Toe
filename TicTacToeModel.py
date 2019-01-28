from os import system
import numpy as np
import random
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class TicTacToeModel:
    def __init__(self, needToWin, GRID_SIZE,player1,player2):
        self.NEED_TO_WIN = needToWin
        self.GRID_SIZE = GRID_SIZE
        self.players = [player1,player2]
        self.board = self.create_board(self.GRID_SIZE)
        self.N = 0
        
    def create_board(self,n):
        return [[0] * n for i in range(n)]

    def check_line(self,board,player,i,j,x,y):
        if(i+(self.NEED_TO_WIN-1)*x < 0 or i+(self.NEED_TO_WIN-1)*x>=self.GRID_SIZE):
            return 0
        if(j+(self.NEED_TO_WIN-1)*y < 0 or j+(self.NEED_TO_WIN-1)*y>=self.GRID_SIZE):
            return 0
        
        flag = 1
        for q in range(self.NEED_TO_WIN):
            if(board[i+q*x][j+q*y]!=player):
                flag = 0
        return flag

    def win(self, board, player):
        all = 0
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                all+=self.check_line(board,player,i,j,0,1)
                all+=self.check_line(board,player,i,j,1,0)
                all+=self.check_line(board,player,i,j,1,1)
                all+=self.check_line(board,player,i,j,1,-1)
                all+=self.check_line(board,player,i,j,-1,1)
        return (all>0)

    def gameover(self,board):
        return self.win(board, 1) or self.win(board, 2) or self.N==self.GRID_SIZE**2

    def tryMakingAMove(self,board,next,turn):
        i = next//self.GRID_SIZE
        j = next%self.GRID_SIZE
        if(board[i][j] == 0):
            board[i][j] = turn
            self.N += 1
            return 1
        else:
            print('Already occupied!')
            return 0