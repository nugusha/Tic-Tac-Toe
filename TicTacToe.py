from os import system
import numpy as np
import pygame
import random
import sys
from TicTacToeView import TicTacToeView

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class TicTacToe:
    def __init__(self, needToWin, GRID_SIZE):
        self.NEED_TO_WIN = needToWin
        self.GRID_SIZE = GRID_SIZE
        self.ROW_COUNT = GRID_SIZE
        self.COLUMN_COUNT = GRID_SIZE
        
        self.View = TicTacToeView(GRID_SIZE)
        self.N = 0
        
    def create_board(self,n):
        return [['.'] * n for i in range(n)]

    def check_line(self,board,player,i,j,x,y):
        if(i+(self.NEED_TO_WIN-1)*x < 0 or i+(self.NEED_TO_WIN-1)*x>=self.ROW_COUNT):
            return 0
        if(j+(self.NEED_TO_WIN-1)*y < 0 or j+(self.NEED_TO_WIN-1)*y>=self.ROW_COUNT):
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
        return self.win(board, 'X') or self.win(board, 'O') or self.N==self.GRID_SIZE**2

    def printBoard(self,board):
        for x in board:
            for y in x:
                print (y, end ='')
            print()
        print()

    def humanTurn(self,board,event):
        posx = event.pos[0]
        posy = event.pos[1]
        col = posx // self.View.SQUARESIZE
        row = posy // self.View.SQUARESIZE - 1
        next = row * self.GRID_SIZE + col
        return next

    def botTurn(self,board):
        x = random.randint(0,self.GRID_SIZE**2-1)
        while(board[x//self.GRID_SIZE][x%self.GRID_SIZE]!='.'):
            x = random.randint(0,self.GRID_SIZE**2-1)
        return x

    def draw_board(self,board):
        self.View.draw_board(board,self.GRID_SIZE)

    def finish(self,board,human,bot,screen,myfont):
        if(self.win(board, human)):
            self.View.headline("You Win!!")
        elif(self.win(board, bot)):
            self.View.headline("You Lose!")
        else:
            self.View.headline("Draw!!!")

    def draw_turn(self,turn,human,myfont,screen):
        self.View.draw_turn(turn,human)

    def run(self):
        self.run2(self.GRID_SIZE,self.View.screen,self.View.myfont)

    def run2(self,GRID_SIZE,screen,myfont):
        human = 'X'
        bot = 'O'
        start = 'X'

        turn = start
        next = 0

        board = self.create_board(GRID_SIZE)
        self.draw_board(board)
        pygame.display.update()

        while(self.gameover(board)==False):
            self.draw_turn(turn,human,myfont,screen)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
                make_turn = False
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if(turn == human):
                        next = self.humanTurn(board,event)
                        make_turn = True
                if(turn == bot):
                    pygame.time.wait(500)
                    next = self.botTurn(board)
                else:
                    if(make_turn == False):
                        continue

                i = next//GRID_SIZE
                j = next%GRID_SIZE
                if(board[i][j] == '.'):
                    board[i][j] = turn
                    self.N += 1
                    self.printBoard(board)
                else:
                    print('Already occupied!')
                    continue

                if(turn == 'X'):
                    turn = 'O'
                else:
                    turn = 'X'
                    
                self.draw_board(board)
                
                if(self.gameover(board)):
                    self.finish(board,human,bot,screen,myfont)
                    pygame.time.wait(3000)
        sys.exit()
    
