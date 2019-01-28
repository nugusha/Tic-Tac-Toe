from os import system
import numpy as np
import pygame
import random
import sys
from TicTacToeView import TicTacToeView
from TicTacToeModel import TicTacToeModel

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class TicTacToe:
    def __init__(self, needToWin, GRID_SIZE,player1,player2):
        self.Model = TicTacToeModel(needToWin,GRID_SIZE,player1,player2)
        self.View = TicTacToeView(GRID_SIZE)
        self.GRID_SIZE = GRID_SIZE
        
    def gameover(self,board):
        self.View.gameover()
        return self.Model.gameover(board)

    def Win(self,board,x):
        return self.Model.win(board, x)

    def printBoard(self,board):
        for x in board:
            for y in x:
                print (y, end ='')
            print()
        print()

    def draw_board(self,board):
        self.View.draw_board(board)

    def finish(self,board,players):
        if(self.Model.win(board, 1)):
            self.View.headline(players[0].name + " Wins!!")
        elif(self.Model.win(board, 2)):
            self.View.headline(players[1].name + " Wins!")
        else:
            self.View.headline("Draw!!!")
        self.View.WAIT(3000)

    def draw_turn(self,player):
        self.View.draw_turn(player.name)

    def run(self):
        players = self.Model.players # [player1,player2]
        turn = 1

        board = self.Model.board
        self.draw_board(board)

        while(self.gameover(board)==False):
            self.draw_turn(players[turn-1])
            next = players[turn-1].make_a_move(board,pygame)

            if(self.Model.tryMakingAMove(board,next,turn)==0):
                continue

            turn = 3 - turn
            self.draw_board(board)

        self.finish(board,players)
        sys.exit()