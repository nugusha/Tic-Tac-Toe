import numpy as np
import math
from TicTacToeModel import TicTacToeModel

class PrioritizeMoves:
    def __init__(self,needtowin,GRID_SIZE):
        self.TModel = TicTacToeModel(needtowin,GRID_SIZE)

    def PrioritizeMoves(self,board,player,moves):
        def do(howmany,double=0):
            new_board = board.copy()
            new_board[move[0]][move[1]] = player
            cnt = self.HVDX(new_board,player,move,howmany) 
            if(howmany==3 and double==1 and cnt>=2):
                return move
            elif(howmany!=3):
                if(cnt>0):
                    return move
                
            new_board = board.copy()
            new_board[move[0]][move[1]] = player*-1
            cnt = self.HVDX_block(new_board,player,move,howmany) 
            if(howmany==3 and double==1 and cnt>=2):
                return move
            elif(howmany!=3):
                if(cnt>0):
                    return move
            return (-1,-1)

        new_moves = []
        new_move = (-1,-1)
        for move in moves:
            new_move = do(5)
            if(new_move != (-1,-1)):
                break
            new_move = do(3,1)
            if(new_move != (-1,-1)):
                break
            new_move = do(4)
            if(new_move != (-1,-1)):
                break
        if(new_move != (-1,-1)):
            return [new_move]

        # for move in moves:
        #         priorityMove = do(4)
        #         if(priorityMove != (-1,-1)):
        #             new_moves.append(priorityMove)
        #         priorityMove = do(3)
        #         if(priorityMove != (-1,-1)):
        #             new_moves.append(priorityMove)
                    
        # for move in moves:
        #         priorityMove = do(2)
        #         if(priorityMove != (-1,-1) and (priorityMove in new_moves) == False):
        #             new_moves.append(priorityMove)
        for move in moves:
            if((move in new_moves) == False):
                new_moves.append(move)
            
        if(len(new_moves)==0):
            new_moves = moves

        #print(new_moves," <===============")
        return new_moves

    # def check_line(self,board,player,i,j,x,y):
    # HVD - horizontal vertical diagonal
    # HVDX - HVD+X - if it can get X marks in line
    def HVDX(self,board,player,move,howmany):
        i = move[0]
        j = move[1]
        TM = self.TModel
        all = 0
        if( TM.check_line(board,player,i,j,0,1,howmany)):
            all += 1
        elif( TM.check_line(board,player,i,j,1,0,howmany)):
            all += 1
        elif( TM.check_line(board,player,i,j,0,-1,howmany)):
            all += 1
        elif( TM.check_line(board,player,i,j,-1,0,howmany)):
            all += 1
        elif( TM.check_line(board,player,i,j,1,1,howmany)):
            all += 1
        elif( TM.check_line(board,player,i,j,1,-1,howmany)):
            all += 1
        elif( TM.check_line(board,player,i,j,-1,-1,howmany)):
            all += 1
        elif( TM.check_line(board,player,i,j,-1,1,howmany)):
            all += 1
        return all
        
    
    def HVDX_block(self,board,player,move,howmany):
        return self.HVDX(board,player*-1,move,howmany)
    
