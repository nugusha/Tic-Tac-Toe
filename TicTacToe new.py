from os import system
import numpy as np
import pygame
import random
import sys


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
        
        self.SQUARESIZE = 300//self.GRID_SIZE
        self.RADIUS = int(self.SQUARESIZE/2-5)
        self.width = self.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.N = 0

        pygame.init()
        
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
        col = posx // self.SQUARESIZE
        row = posy // self.SQUARESIZE - 1
        next = row * self.GRID_SIZE + col
        return next

    def botTurn(self,board):
        x = random.randint(0,self.GRID_SIZE**2-1)
        while(board[x//self.GRID_SIZE][x%self.GRID_SIZE]!='.'):
            x = random.randint(0,self.GRID_SIZE**2-1)
        return x

    def draw_board(self,board,screen):
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c*self.SQUARESIZE,(r+1)*self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE ))
                if( board[r][c] == 'X'):
                    color = YELLOW
                if( board[r][c] == 'O'):
                    color = RED
                if( board[r][c] == '.'):
                    color = WHITE
                
                pygame.draw.circle(screen, color, (int(c*self.SQUARESIZE+self.SQUARESIZE/2),int((r+1)*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
                pygame.display.update()

    def finish(self,board,human,bot,screen,myfont):
        pygame.draw.rect(screen, BLACK, (0,0,self.width,self.SQUARESIZE))
        if(self.win(board, human)):
            print('You Win!!!')
            label = myfont.render("You Win!!", 1 , YELLOW)
            screen.blit(label, (25, 10))
        elif(self.win(board, bot)):
            print('You Lose')
            label = myfont.render("You Lose!!", 1 , RED)
            screen.blit(label, (25, 10))
        else:
            print('Draw')
            label = myfont.render("Draw!!", 1 , BLUE)
            screen.blit(label, (25, 10))
        pygame.display.update()

    def draw_turn(self,turn,human,myfont,screen):
        pygame.draw.rect(screen, BLACK, (0,0,self.width,self.SQUARESIZE))
        if(turn == human):
            label = myfont.render("Your Turn!", 1 , YELLOW)
            screen.blit(label, (25, 10))
        else:
            label = myfont.render("Bot Turn!", 1 , YELLOW)
            screen.blit(label, (25, 10))
        pygame.display.update()

    def run(self):
        self.run2(self.GRID_SIZE,self.SQUARESIZE,self.size)

    def run2(self,GRID_SIZE,SQUARESIZE,size):
        screen = pygame.display.set_mode(size)
        myfont = pygame.font.SysFont("monospace", SQUARESIZE//2)
        human = 'X'
        bot = 'O'
        start = 'X'

        turn = start
        next = 0

        board = self.create_board(GRID_SIZE)
        self.draw_board(board,screen)
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
                    
                self.draw_board(board,screen)
                
                if(self.gameover(board)):
                    self.finish(board,human,bot,screen,myfont)
                    pygame.time.wait(3000)

if __name__ == '__main__':
    A_TicTacToe = TicTacToe(3,3)
    A_TicTacToe.run()
