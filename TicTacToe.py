from os import system
import numpy as np
import pygame
import random
import sys
from TicTacToeView import TicTacToeView
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class TicTacToe:
    def __init__(self, needToWin, GRID_SIZE,player1,player2):
        self.NEED_TO_WIN = needToWin
        self.GRID_SIZE = GRID_SIZE
        self.player1 = player1
        self.player2 = player2
        self.ROW_COUNT = GRID_SIZE
        self.COLUMN_COUNT = GRID_SIZE
        
        self.View = TicTacToeView(GRID_SIZE)
        self.N = 0
        
    def create_board(self,n):
        return [[0] * n for i in range(n)]

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
        return self.win(board, 1) or self.win(board, 2) or self.N==self.GRID_SIZE**2

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

    def draw_board(self,board):
        self.View.draw_board(board,self.GRID_SIZE)

    def finish(self,board,human,bot,screen,myfont):
        if(self.win(board, human)):
            self.View.headline("Player 1 Wins!!")
        elif(self.win(board, bot)):
            self.View.headline("Player 2 Wins!")
        else:
            self.View.headline("Draw!!!")

    def draw_turn(self,turn,myfont,screen):
        self.View.draw_turn(turn)

    def run(self):
        self.run2(self.GRID_SIZE,self.View.screen,self.View.myfont)

    def run2(self,GRID_SIZE,screen,myfont):
        human = 1
        bot = 2
        start = 1

        player1 = self.player1() 
        player2 = self.player2()
        turn = start
        next = 0

        board = self.create_board(GRID_SIZE)
        self.draw_board(board)
        pygame.display.update()

        while(self.gameover(board)==False):
            print(turn,human)
            self.draw_turn(turn,myfont,screen)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
                
            if(turn == human):
                next = player1.make_a_move(board,pygame,self.View.SQUARESIZE)
            else:
                next = player2.make_a_move(board,pygame,self.View.SQUARESIZE)

            i = next//GRID_SIZE
            j = next%GRID_SIZE
            if(board[i][j] == 0):
                board[i][j] = turn
                self.N += 1
                self.printBoard(board)
            else:
                print('Already occupied!')
                continue

            if(turn == 1):
                turn = 2
            else:
                turn = 1
                
            self.draw_board(board)
            
            if(self.gameover(board)):
                self.finish(board,human,bot,screen,myfont)
                pygame.time.wait(3000)
                sys.exit()
        sys.exit()
    
