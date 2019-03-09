
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class TicTacToeModel:
    def __init__(self, needToWin, GRID_SIZE,player1=0,player2=0):
        self.NEED_TO_WIN = needToWin
        self.GRID_SIZE = GRID_SIZE
        self.players = [player1,player2]
        self.N = 0
        
    def create_board(self):
        n = self.GRID_SIZE
        return [[0] * n for i in range(n)]

    def check_line(self,board,player,i,j,x,y,howmany=-1):
        if(howmany==-1):
            howmany = self.NEED_TO_WIN
        if(i+(howmany-1)*x < 0 or i+(howmany-1)*x>=self.GRID_SIZE):
            return 0
        if(j+(howmany-1)*y < 0 or j+(howmany-1)*y>=self.GRID_SIZE):
            return 0
        
        flag = 1
        for q in range(howmany):
            if(board[i+q*x][j+q*y]!=player):
                flag = 0
        return flag

    def check_line2(self, board, player, ii, jj, lastmove):
        c_i,c_j = lastmove
        x = 0
        i,j = c_i,c_j
        while(board[i][j]==player):
            x +=1
            i += ii
            j += jj
            if(j>=len(board) or i>=len(board) or j<0 or i<0):
                break
            
        i,j = c_i,c_j
        while(board[i][j]==player):
            x +=1
            i -= ii
            j -= jj
            if(j>=len(board) or i>=len(board) or j<0 or i<0):
                break
        return x-(board[c_i][c_j]==player)

    def win(self, board, player, lastmove = None):
        if(lastmove!=None):
            cnt_hor = self.check_line2(board,player,0,1,lastmove)
            cnt_ver = self.check_line2(board,player,1,0,lastmove)
            cnt_diag = self.check_line2(board,player,1,1,lastmove)
            cnt_diagrev = self.check_line2(board,player,1,-1,lastmove)
            
            if(cnt_hor>=self.NEED_TO_WIN or cnt_ver>=self.NEED_TO_WIN or cnt_diag>self.NEED_TO_WIN or cnt_diagrev>self.NEED_TO_WIN):
                return True
            return False
            
        all = 0
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if( self.check_line(board,player,i,j,0,1)): 
                    all+=1
                elif( self.check_line(board,player,i,j,1,0)): 
                    all+=1
                elif( self.check_line(board,player,i,j,1,1)): 
                    all+=1
                elif( self.check_line(board,player,i,j,1,-1)): 
                    all+=1
        return (all>0)

    def gameover(self,board, lastmove = None):
        flag = 1
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if(board[i][j]==0):
                    flag = 0
                    break
            if(flag == 0):
                break
        
        return self.win(board, 1, lastmove) or self.win(board, -1, lastmove) or flag

    def tryMakingAMove(self,board,next,turn):
        i = next//self.GRID_SIZE
        j = next%self.GRID_SIZE
        if(board[i][j] == 0):
            board[i][j] = turn
            self.N += 1
            return 1
        else:
            print('Already occupied!')
            return 0