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
    def __init__(self, needToWin, GRID_SIZE,player1,player2):
        self.NEED_TO_WIN = needToWin
        self.GRID_SIZE = GRID_SIZE
        self.players = [player1,player2]
        self.board = self.create_board(self.GRID_SIZE)

        self.View = TicTacToeView(GRID_SIZE)
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
        self.View.gameover()
        return self.win(board, 1) or self.win(board, 2) or self.N==self.GRID_SIZE**2

    def printBoard(self,board):
        for x in board:
            for y in x:
                print (y, end ='')
            print()
        print()

    def draw_board(self,board):
        self.View.draw_board(board)

    def finish(self,board,players):
        if(self.win(board, 1)):
            self.View.headline(players[0].name + " Wins!!")
        elif(self.win(board, 2)):
            self.View.headline(players[1].name + " Wins!")
        else:
            self.View.headline("Draw!!!")
        self.View.WAIT(3000)

    def draw_turn(self,player):
        self.View.draw_turn(player.name)

    def tryMakingAMove(self,board,next,turn):
        i = next//self.GRID_SIZE
        j = next%self.GRID_SIZE
        if(board[i][j] == 0):
            board[i][j] = turn
            self.N += 1
            self.printBoard(board)
            return 1
        else:
            print('Already occupied!')
            return 0

    def run(self):
        players = self.players # [player1,player2]
        turn = 1

        board = self.board
        self.draw_board(board)

        while(self.gameover(board)==False):
            self.draw_turn(players[turn-1])
            next = players[turn-1].make_a_move(board,pygame)

            if(self.tryMakingAMove(board,next,turn)==0):
                continue

            turn = 3 - turn
            self.draw_board(board)

        self.finish(board,players)
        sys.exit()