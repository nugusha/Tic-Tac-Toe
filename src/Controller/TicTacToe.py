from os import system
import numpy as np
import pygame
import random
import sys
import time
sys.path.append('./View')
from TicTacToeView import TicTacToeView
sys.path.append('./Model')
from TicTacToeModel import TicTacToeModel

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
needToWinGLOBAL = 0
class TicTacToe:
    def __init__(self, needToWin, GRID_SIZE,player1,player2):
        global needToWinGLOBAL
        needToWinGLOBAL = needToWin
        self.NEED_TO_WIN = needToWin
        self.Model = TicTacToeModel(needToWin,GRID_SIZE,player1,player2)
        self.View = TicTacToeView(GRID_SIZE)
        self.GRID_SIZE = GRID_SIZE
        
    def gameover(self,board):
        self.View.gameover()
        return self.Model.gameover(board)
    
    def Win(self,board,x):
        return self.Model.win(board, x)

    def Status(self,board):
        if(self.Win(board,1)>0):
            return 1
        if(self.Win(board,-1)>0):
            return -1
        if(self.gameover(board)>0):
            return 0
        return None

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
        elif(self.Model.win(board, -1)):
            self.View.headline(players[1].name + " Wins!")
        else:
            self.View.headline("Draw!!!")
        if(len(board)==3):
            self.View.WAIT(3000)
        else:
            self.View.WAIT(30000)

    def draw_turn(self,player):
        self.View.draw_turn(player.name)

    def run(self):
        players = self.Model.players # [player1,player2]
        turn = 1
        Log = []

        board = self.Model.board
        self.draw_board(board)

        while(self.gameover(board)==False):
            self.draw_turn(players[turn!=1])
            start = time.time()
            next = players[(turn!=1)].make_a_move(board,pygame)
            end = time.time()
            print(end - start)
            
            if(self.Model.tryMakingAMove(board,next,turn)==0):
                continue

            move_now = [next//self.GRID_SIZE,next%self.GRID_SIZE]
            print(move_now)
            Log.append(move_now)
            
            turn *= -1
            self.draw_board(board)

        self.finish(board,players)
        print(Log)
        sys.exit()
class TicTacToeStatic:
    @staticmethod
    def available_moves(s):
        m = []
        length = len(s)
        for i in range(length):
            for j in range(length):
                if(s[i,j]==0):
                    m.append((i,j))
        return m
    
    @staticmethod
    def Status(s):
        if(len(s)!=3):                
            TTT = TicTacToe(needToWinGLOBAL,len(s),None,None)
            return TTT.Status(s)

        all = []
        for x in s.tolist():
            all.append(x)
        for x in [list(i) for i in zip(*s)]:
            all.append(x)

        all.append([s[0,0],s[1,1],s[2,2]])
        all.append([s[2,0],s[1,1],s[0,2]])

        e = 0

        if [1, 1, 1] in all:
            e = 1
        elif [-1, -1, -1] in all:
            e = -1 
        else:            
            for i in range(3):
                for j in range(3):
                    if(s[i,j]==0):
                        e = None                        
        return e
    
    @staticmethod
    def nearest(s,r,c):
        mi = 999999999
        length = len(s)
        for i in range(length):
            for j in range(length):
                if(s[i][j]!=0):
                    mi = min(mi,abs(i-r)+abs(j-c))
        if(mi == 999999999):
            mi = 0
        return mi

    @staticmethod
    def getNTW():
        return needToWinGLOBAL

    @staticmethod
    def removecopies(s,m):
        boards = []
        copies = []
        newboards = []
        
        for i in range(len(m)):
            move = m[i]
            new_s = s.copy()
            r = move[0]
            c = move[1]
            new_s[r][c] = 10
            if(TicTacToeStatic.nearest(s,r,c)>2):
                copies.append(i)
            boards.append(new_s)
            new_s=None

        if(len(s)!=10):
            for i in range(len(m)):
                for j in range(len(m)):
                    if(i>=j or i in copies or j in copies):
                        continue
                    if(np.array_equal(boards[i],np.flipud(boards[j]))):
                        copies.append(j)
                    elif(np.array_equal(boards[i],np.fliplr(boards[j]))):
                        copies.append(j)
                    elif(np.array_equal(boards[i],np.rot90(boards[j]))):
                        copies.append(j)
                    elif(np.array_equal(boards[i],np.rot90(np.rot90(boards[j])))):
                        copies.append(j)
                    elif(np.array_equal(boards[i],np.rot90(np.rot90(np.rot90(boards[j]))))):
                        copies.append(j)
        
        for i in range(len(m)):
            if(i in copies):
                continue
            newboards.append(m[i])
        
        return newboards