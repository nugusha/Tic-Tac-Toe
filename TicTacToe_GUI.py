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
NEED_TO_WIN = 5
GRID_SIZE = 10
ROW_COUNT = GRID_SIZE
COLUMN_COUNT = GRID_SIZE

def create_board(n):
    return [['.'] * n for i in range(n)]

def check_line(board,player,i,j,x,y):
    if(i+(NEED_TO_WIN-1)*x < 0 or i+(NEED_TO_WIN-1)*x>=ROW_COUNT):
        return 0
    if(j+(NEED_TO_WIN-1)*y < 0 or j+(NEED_TO_WIN-1)*y>=ROW_COUNT):
        return 0
    
    flag = 1
    for q in range(NEED_TO_WIN):
        if(board[i+q*x][j+q*y]!=player):
            flag = 0
    return flag

def win(board, player):
    all = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            all+=check_line(board,player,i,j,0,1)
            all+=check_line(board,player,i,j,1,0)
            all+=check_line(board,player,i,j,1,1)
            all+=check_line(board,player,i,j,1,-1)
            all+=check_line(board,player,i,j,-1,1)
    return (all>0)

def gameover(board):
    return win(board, 'X') or win(board, 'O') or N==GRID_SIZE**2

def printBoard(board):
    for x in board:
        for y in x:
            print (y, end ='')
        print()
    print()

def humanTurn(board):
    posx = event.pos[0]
    posy = event.pos[1]
    col = posx // SQUARESIZE
    row = posy // SQUARESIZE - 1
    next = row * GRID_SIZE + col
    return next

def botTurn(board):
    x = random.randint(0,GRID_SIZE**2-1)
    while(board[x//GRID_SIZE][x%GRID_SIZE]!='.'):
        x = random.randint(0,GRID_SIZE**2-1)
    return x

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE,(r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE ))
            if( board[r][c] == 'X'):
                color = YELLOW
            if( board[r][c] == 'O'):
                color = RED
            if( board[r][c] == '.'):
                color = WHITE
            
            pygame.draw.circle(screen, color, (int(c*SQUARESIZE+SQUARESIZE/2),int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            pygame.display.update()

def finish():
    pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
    if(win(board, human)):
        print('You Win!!!')
        label = myfont.render("You Win!!", 1 , YELLOW)
        screen.blit(label, (25, 10))
    elif(win(board, bot)):
        print('You Lose')
        label = myfont.render("You Lose!!", 1 , RED)
        screen.blit(label, (25, 10))
    else:
        print('Draw')
        label = myfont.render("Draw!!", 1 , BLUE)
        screen.blit(label, (25, 10))
    pygame.display.update()

def draw_turn():
    pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
    if(turn == human):
        label = myfont.render("Your Turn!", 1 , YELLOW)
        screen.blit(label, (25, 10))
    else:
        label = myfont.render("Bot Turn!", 1 , YELLOW)
        screen.blit(label, (25, 10))
    pygame.display.update()

human = 'X'
bot = 'O'
start = 'X'

turn = start
N = 0
next = 0

SQUARESIZE = 600//GRID_SIZE
RADIUS = int(SQUARESIZE/2-5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", SQUARESIZE//2)

game_over = False
board = create_board(GRID_SIZE)
draw_board(board)
pygame.display.update()

while(gameover(board)==False):
    draw_turn()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
        make_turn = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(turn == human):
                next = humanTurn(board)
                make_turn = True
        if(turn == bot):
            pygame.time.wait(500)
            next = botTurn(board)
        else:
            if(make_turn == False):
                continue

        i = next//GRID_SIZE
        j = next%GRID_SIZE
        if(board[i][j] == '.'):
            board[i][j] = turn
            N += 1
            printBoard(board)
        else:
            print('Already occupied!')
            continue

        if(turn == 'X'):
            turn = 'O'
        else:
            turn = 'X'
            
        draw_board(board)
        
        if(gameover(board)):
            finish()
            pygame.time.wait(3000)

    

#if __name__ == '__main__':
#    main()
