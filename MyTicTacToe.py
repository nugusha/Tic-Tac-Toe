from os import system
import random


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
    return win(board, 'X') or win(board, 'O')

def printBoard(board):
    for x in board:
        for y in x:
            print (y, end ='')
        print()
    print()
def humanTurn(board):
    next = -1
    while(0>next or next>=9):
        try:
            next = int(input('Input 1-9 '))-1
            if(0>next or next>=9):
                print('Wrong number')
        except KeyboardInterrupt:
            print('Adios')
            exit()
        except:
            print('Wrong charracter')
    return next
def botTurn(board):
    x = random.randint(0,8)
    while(board[x//3][x%3]!='.'):
        x = random.randint(0,8)
    return x
def main():
    n = 3
    human = ''
    bot = ''
    start = ''
    
    while(human!='X' and human!='O'):
        try:
            system('cls')
            human = input('Choose X or O\n').upper()
        except:
            exit()
    
    if(human == 'X'):
        bot = 'O'
    else:
        bot = 'X'

    while(start!='y' and start!='n'):
        try:
            system('cls')
            start = input('Do you want to start?[y\\n]\n').lower()
        except:
            exit()

    if(start == 'y'):
        start = human
    else:
        start = bot

    print('HUMAN =', human)
    print('BOT =', bot)
    print('Starts -', start)
    print()

    board = [['.'] * n for i in range(n)]


    turn = start
    N = 0
    next = 0

    while(gameover(board)==False):
        if(turn == human):
            next = humanTurn(board)
        if(turn == bot):
            next = botTurn(board)

        i = next//3
        j = next%3
        if(board[i][j] == '.'):
            board[i][j] = turn
            N += 1
            printBoard(board)
        else:
            print('Already occupied!')
            continue

        if(N == 9):
            break        

        if(turn == 'X'):
            turn = 'O'
        else:
            turn = 'X'

    if(win(board, human)):
        print('You Win!!!')
    elif(win(board, bot)):
        print('You Lose')
    else:
        print('Draw')

    exit()


if __name__ == '__main__':
    main()
