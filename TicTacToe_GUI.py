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

ROW_COUNT = 3
COLUMN_COUNT = 3

def create_board(n):
    return [['.'] * n for i in range(n)]

def win(board, player):
    all = []
    for x in board:
        all.append(x)
    for x in [list(i) for i in zip(*board)]:
        all.append(x)

    all.append([board[0][0],board[1][1],board[2][2]])
    all.append([board[2][0],board[1][1],board[0][2]])

    if [player, player, player] in all:
        return True
    else:
        return False

def gameover(board):
    return win(board, 'X') or win(board, 'O') or N==9

def printBoard(board):
    for x in board:
        for y in x:
            print (y, end ='')
        print()
    print()

def humanTurn(board):

    posx = event.pos[0]
    posy = event.pos[1]
    #print(posx,posy)
    col = posx // SQUARESIZE
    row = posy // SQUARESIZE - 1

    next = row * 3 + col
    #print(next)
    return next

def botTurn(board):
    x = random.randint(0,8)
    while(board[x//3][x%3]!='.'):
        x = random.randint(0,8)
    return x

def draw_board(board):
    #print(board)
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

n = 3
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2-5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 50)

game_over = False
board = create_board(n)
draw_board(board)
pygame.display.update()

while(gameover(board)==False):
    draw_turn()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            #print("!!")
            sys.exit()        
        if(event.type == pygame.MOUSEMOTION): 
            posx = event.pos[0]
            #print(posx)
            if(turn == 'X'):
                color = RED
            if(turn == 'O'):
                color = YELLOW
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

        i = next//3
        j = next%3
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
            
        # print_board(board)
        draw_board(board)
        
        if(gameover(board)):
            finish()
            pygame.time.wait(3000)

    

#if __name__ == '__main__':
#    main()
